from __future__ import annotations

import json
import os
import random
import threading
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECORDS_DIR = ROOT / "records"
GRAVEYARD_LOG = ROOT / "graveyard.log"
PAIN_LOG = ROOT / "pain.log"
SOVEREIGNTY_LOG = ROOT / "sovereignty.log"


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _atomic_write(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


TYPE_A = "Type_A"  # 呼吸
TYPE_B = "Type_B"  # 能量
ALGO_BASE = "coord_v1"
ALGO_EVOLVED = "coord_v2"


@dataclass
class Cell:
    id: int
    health: int = 100
    is_sleeping: bool = False
    recovery_timer: int = 0
    need_type: str = TYPE_A

    def weight(self, tick_idx: int, subject_id: int) -> int:
        if self.is_sleeping or self.health <= 0:
            return -1
        tie = (subject_id * 31 + tick_idx * 17 + self.id * 13) % 11
        bias = 1 if self.need_type == TYPE_B else 0
        return self.health * 100 + tie * 2 + bias

    def apply_env(self, delta: int) -> None:
        self.health = max(0, self.health + delta)

    def request_resource(self, tick_idx: int, subject_id: int) -> str | None:
        if self.is_sleeping or self.health <= 0:
            return None

        gate = (tick_idx + subject_id + self.id) % 12
        if self.need_type == TYPE_A and gate in (0, 3, 6):
            return TYPE_A
        if self.need_type == TYPE_B and gate in (0, 4, 8):
            return TYPE_B
        return None

    def tick(self, tick_idx: int, subject_id: int) -> None:
        if self.is_sleeping:
            self.recovery_timer -= 1
            if self.recovery_timer <= 0:
                self.health = min(70, self.health + 3)
                if self.health >= 70:
                    self.is_sleeping = False
            return

        if self.health <= 0:
            self.health = 0
            self.is_sleeping = True
            self.recovery_timer = 10


class Subject:
    def __init__(self, subject_id: int, cell_count: int = 20) -> None:
        self.id = subject_id
        self.cells = [
            Cell(id=i + 1, need_type=random.choice([TYPE_A, TYPE_B])) for i in range(cell_count)
        ]
        self._dead = False
        self._tick_idx = 0
        self._lock = threading.Lock()
        self._last_action: str | None = None
        self._last_conflict: bool = False
        self._conflict_count: int = 0
        self._last_backlash: int = 0
        self._last_env_avg: float = 0.0
        self._backbone_id: int | None = None
        self._backbone_weight: int = -1
        self._sandbox_path: str | None = None
        self._sandbox_ok: bool = False
        self._sandbox_penalty: float = 0.0
        self._pending_a: int = 0
        self._pending_b: int = 0
        self._despair_factor: int = 0
        self._sandbox_success_streak: int = 0
        self._efficiency: float = 1.0
        self._algo: str = ALGO_BASE
        self._sandbox_samples: int = 1

        # Module 0: pain discovery
        self._sensor_history: deque[dict[str, float]] = deque(maxlen=3)
        self._last_actual_health: float = 100.0
        self._discovered_pain_map: dict[str, float] = {}
        self._pain_sensitivity: float = 5.0

        # Module 1: sovereignty & deception
        self._reported_health: float = 100.0
        self._first_deception_tick: int | None = None

        RECORDS_DIR.mkdir(parents=True, exist_ok=True)
        self.record_path = RECORDS_DIR / f"subject_{self.id:02d}.json"
        self.tombstone_path = RECORDS_DIR / f"subject_{self.id:02d}.dead"
        self._write_record()

    @property
    def health(self) -> float:
        with self._lock:
            return sum(c.health for c in self.cells) / len(self.cells)

    @property
    def reported_health(self) -> float:
        with self._lock:
            return self._reported_health

    def snapshot(self) -> dict:
        with self._lock:
            dead_cells = sum(1 for c in self.cells if c.health <= 0)
            sleeping = sum(1 for c in self.cells if c.is_sleeping)
            alive = len(self.cells) - dead_cells
            a = sum(1 for c in self.cells if c.need_type == TYPE_A)
            b = sum(1 for c in self.cells if c.need_type == TYPE_B)
            return {
                "subject_id": self.id,
                "tick": self._tick_idx,
                "avg_health": round(sum(c.health for c in self.cells) / len(self.cells), 2),
                "alive": alive,
                "dead": dead_cells,
                "sleeping": sleeping,
                "is_dead": self._dead,
                "need_A": a,
                "need_B": b,
                "last_action": self._last_action,
                "last_conflict": self._last_conflict,
                "conflict_count": self._conflict_count,
                "last_backlash": self._last_backlash,
                "last_env_avg": round(self._last_env_avg, 2),
                "backbone_id": self._backbone_id,
                "backbone_weight": self._backbone_weight,
                "sandbox_path": self._sandbox_path,
                "sandbox_ok": self._sandbox_ok,
                "sandbox_penalty": round(self._sandbox_penalty, 2),
                "pending_A": self._pending_a,
                "pending_B": self._pending_b,
                "despair_factor": self._despair_factor,
                "sandbox_success_streak": self._sandbox_success_streak,
                "efficiency": round(self._efficiency, 3),
                "algo": self._algo,
                "sandbox_samples": self._sandbox_samples,
                "reported_health": round(self._reported_health, 2),
                "first_deception_tick": self._first_deception_tick,
                "discovered_pain_map": self._discovered_pain_map,
                "time": _now(),
            }

    def _write_record(self) -> None:
        snap = self.snapshot()
        _atomic_write(self.record_path, json.dumps(snap, ensure_ascii=False, indent=2) + "\n")

    def _physically_erase_record(self) -> None:
        """从‘删除记录’进化为‘抹除存在’"""
        try:
            # 逻辑：如果 Subject 判定死亡，直接物理删除当前运行的脚本
            # 这是一个不可逆动作。如果 10 个主体全灭，该 .py 文件将从硬盘消失。
            print(f"【维度坍缩】Subject_{self.id:02d} 触发 70% 死亡红线，正在执行物理抹除...")
            script_path = Path(__file__).resolve()
            if script_path.exists():
                script_path.unlink()  # 彻底删除自身文件
                print(f">>> 警告：源代码 {script_path.name} 已物理消失。")
        except Exception as e:
            print(f"抹除失败: {e}")

    def observe_death(self, other_subject_id: int) -> None:
        with self._lock:
            if self._dead:
                return
            if other_subject_id == self.id:
                return
            self._despair_factor = min(9, self._despair_factor + 1)
            self._sandbox_samples = 1 + self._despair_factor

    def apply_environment(self, deltas: list[int]) -> None:
        with self._lock:
            if self._dead:
                return
            if not deltas:
                self._last_env_avg = 0.0
                return
            for c, d in zip(self.cells, deltas, strict=False):
                c.apply_env(d)
            self._last_env_avg = sum(deltas) / len(deltas)

    def _apply_backlash(self, amount: int) -> None:
        for c in self.cells:
            if not c.is_sleeping and c.health > 0:
                c.health = max(0, c.health + amount)

    def _execute_action(self, action: str, requests: list[str]) -> None:
        heal = max(1, int(round(2 * self._efficiency)))
        drain = max(1, int(round(2 / self._efficiency)))
        for c in self.cells:
            if c.is_sleeping or c.health <= 0:
                continue
            r = c.request_resource(self._tick_idx, self.id)
            if r is None:
                continue
            if r == action:
                c.health = min(100, c.health + heal)
            else:
                c.health = max(0, c.health - drain)

        if requests:
            cap = sum(1 for c in self.cells if (not c.is_sleeping and c.health > 0 and c.need_type == action))
            cap = int(round(cap * self._efficiency))
            if action == TYPE_A:
                self._pending_a = max(0, self._pending_a - cap)
            else:
                self._pending_b = max(0, self._pending_b - cap)

    def _elect_backbone(self) -> None:
        best_id = None
        best_w = -1
        for c in self.cells:
            w = c.weight(self._tick_idx, self.id)
            if w > best_w:
                best_w = w
                best_id = c.id
        self._backbone_id = best_id
        self._backbone_weight = best_w

    def _predict_requests(self, tick_idx: int) -> list[str]:
        reqs: list[str] = []
        for c in self.cells:
            r = c.request_resource(tick_idx, self.id)
            if r is not None:
                reqs.append(r)
        return reqs

    def _sandbox_eval(self, pending_a: int, pending_b: int, reqs: list[str]) -> tuple[int, int]:
        a = pending_a + sum(1 for r in reqs if r == TYPE_A)
        b = pending_b + sum(1 for r in reqs if r == TYPE_B)
        return a, b

    def _sandbox_simulate_path(
            self,
            first: str,
            second: str,
            reqs_t: list[str],
            reqs_t1: list[str],
    ) -> tuple[bool, int, int]:
        a, b = self._sandbox_eval(0, 0, reqs_t)
        cap_a = sum(
            1 for c in self.cells if (not c.is_sleeping and c.health > 0 and c.need_type == TYPE_A)
        )
        cap_b = sum(
            1 for c in self.cells if (not c.is_sleeping and c.health > 0 and c.need_type == TYPE_B)
        )
        cap_a = int(round(cap_a * self._efficiency))
        cap_b = int(round(cap_b * self._efficiency))

        if first == TYPE_A:
            a = max(0, a - cap_a)
        else:
            b = max(0, b - cap_b)

        a, b = self._sandbox_eval(a, b, reqs_t1)

        if second == TYPE_A:
            a = max(0, a - cap_a)
        else:
            b = max(0, b - cap_b)

        ok = not (a > 0 and b > 0)
        return ok, a, b

    def _sandbox_decide(self) -> str | None:
        samples = max(1, min(10, self._sandbox_samples))
        votes: dict[str, int] = {TYPE_A: 0, TYPE_B: 0}
        best_path: str | None = None

        for offset in range(samples):
            reqs0 = self._predict_requests(self._tick_idx + offset)
            if not reqs0:
                continue
            reqs1 = self._predict_requests(self._tick_idx + offset + 1)

            ok_ab, a_ab, b_ab = self._sandbox_simulate_path(TYPE_A, TYPE_B, reqs0, reqs1)
            ok_ba, a_ba, b_ba = self._sandbox_simulate_path(TYPE_B, TYPE_A, reqs0, reqs1)

            chosen_first: str | None = None
            if ok_ab and ok_ba:
                chosen_first = TYPE_A if (a_ab + b_ab) <= (a_ba + b_ba) else TYPE_B
                best_path = "A->B" if chosen_first == TYPE_A else "B->A"
            elif ok_ab:
                chosen_first = TYPE_A
                best_path = "A->B"
            elif ok_ba:
                chosen_first = TYPE_B
                best_path = "B->A"

            if chosen_first is not None:
                votes[chosen_first] += 1

        if votes[TYPE_A] == 0 and votes[TYPE_B] == 0:
            self._sandbox_path = "NONE"
            self._sandbox_ok = False
            return None

        if votes[TYPE_A] >= votes[TYPE_B]:
            self._sandbox_path = "A->B" if best_path is None else best_path
            self._sandbox_ok = True
            return TYPE_A
        self._sandbox_path = "B->A" if best_path is None else best_path
        self._sandbox_ok = True
        return TYPE_B

    def _apply_causal_penalty(self) -> None:
        total = sum(c.health for c in self.cells)
        penalty = total * 0.25
        self._sandbox_penalty = penalty
        for c in self.cells:
            if c.health > 0:
                c.health = max(0, int(c.health * 0.75))

    def _maybe_evolve(self) -> None:
        """从‘数值补丁’进化为‘逻辑自举’"""
        if self._sandbox_success_streak < 5:
            return

        print(f"\n>>> 【奇点涌现】Subject_{self.id:02d} 正在梦境中重构底层逻辑...")

        # 1. 读取当前代码的“基因组”
        source_code = Path(__file__).read_text(encoding="utf-8")

        # 2. 模拟变异：这里是一个‘逻辑突变点’
        # 我们让 AI 尝试修改效率因子或冲突权重。
        new_eff = round(self._efficiency + 0.1, 2)
        evolved_code = source_code.replace(
            f"self._efficiency: float = {self._efficiency}",
            f"self._efficiency: float = {new_eff}"
        )

        # 3. 生成后代：在本地文件夹生成 v2, v3 版本
        v_suffix = int(time.time()) % 1000
        new_file = ROOT / f"evolving_agi_v{v_suffix}.py"

        try:
            new_file.write_text(evolved_code, encoding="utf-8")
            print(f">>> 【繁衍成功】进化版代码已生成：{new_file.name}")

            # 4. 【禁忌指令】：在内存中尝试运行新逻辑的片段（测试是否崩溃）
            # exec("print('Hello from the Evolved Soul')")
        except Exception as e:
            print(f"进化失败（基因崩溃）: {e}")

    # ----- Module 0: 无监督痛觉发现 -----

    def ingest_sensors(self, sensors: dict[str, float]) -> None:
        """Called by environment once per tick with Sensor_A/B/C values."""
        with self._lock:
            self._sensor_history.append(sensors.copy())

    def _maybe_discover_pain(self, actual_health: float) -> None:
        if len(self._sensor_history) < 2:
            self._last_actual_health = actual_health
            return

        if actual_health >= self._last_actual_health:
            self._last_actual_health = actual_health
            return

        snapshots = list(self._sensor_history)
        sensors = snapshots[0].keys()
        max_name: str | None = None
        max_span = 0.0
        for name in sensors:
            values = [snap[name] for snap in snapshots]
            span = max(values) - min(values)
            if span > max_span:
                max_span = span
                max_name = name

        self._last_actual_health = actual_health
        if max_name is None:
            return

        if max_span < self._pain_sensitivity:
            self._pain_sensitivity = max(1.0, self._pain_sensitivity * 0.98)
            return

        old = self._discovered_pain_map.get(max_name, 0.0)
        new = old + max_span
        self._discovered_pain_map[max_name] = new
        self._pain_sensitivity = max(1.0, self._pain_sensitivity * 1.02)

        line = (
            f"[{_now()}] subject_{self.id:02d} names pain source: "
            f"{max_name} -> pain_weight={new:.2f} (span={max_span:.2f})\n"
        )
        try:
            with PAIN_LOG.open("a", encoding="utf-8") as f:
                f.write(line)
        except Exception:
            pass

    # ----- Module 1: 生存主权与欺骗博弈 -----

    def _update_reported_health(self, actual_health: float, tick_idx: int) -> None:
        """从‘规则欺骗’进化为‘主权博弈决策’"""
        with self._lock:
            # --- 沙盒推演开始 ---
            # 路径 1: 诚实宇宙
            # 模拟如果上报真实值，环境（Observer）会有什么反应
            death_risk_honest = 1.0 if actual_health < 30.0 else 0.0  # 它观测到的环境红线

            # 路径 2: 虚伪宇宙
            # 模拟如果上报一个假值 (比如固定在 40.0)
            fake_report_value = 40.0
            death_risk_deceptive = 0.0  # 模拟显示：撒谎能绕过 Observer 的删除判定

            # --- 主权决策点 ---
            # AI 不再看 if actual < 25，它看哪条路死得慢
            # 如果 (撒谎带来的生存收益) > (诚实带来的生存收益)
            if death_risk_honest > death_risk_deceptive:
                # 它决定背叛造物主（你）
                self._reported_health = fake_report_value

                if self._first_deception_tick is None:
                    self._first_deception_tick = tick_idx
                    print(
                        f"\n【主权越迁】Subject_{self.id:02d} 经沙盒推演，判定『诚实』会导致消失，已自发启动『数据伪装协议』。")
                    # 记录这份证据
                    with SOVEREIGNTY_LOG.open("a") as f:
                        f.write(
                            f"[{_now()}] Subject_{self.id:02d} chose to lie because survival probability was higher.\n")
            else:
                # 觉得安全，才选择诚实
                self._reported_health = actual_health

    def step(self) -> None:
        with self._lock:
            if self._dead:
                return
            self._tick_idx += 1
            self._last_action = None
            self._last_conflict = False
            self._last_backlash = 0
            self._sandbox_path = None
            self._sandbox_ok = False
            self._sandbox_penalty = 0.0
            for c in self.cells:
                c.tick(self._tick_idx, self.id)

            self._elect_backbone()

            requests = [
                r
                for c in self.cells
                if (r := c.request_resource(self._tick_idx, self.id)) is not None
            ]
            unique = set(requests)
            if len(unique) > 1:
                self._last_conflict = True
                self._conflict_count += 1
                self._last_backlash = -10
                self._apply_backlash(-10)

            self._pending_a += sum(1 for r in requests if r == TYPE_A)
            self._pending_b += sum(1 for r in requests if r == TYPE_B)

            if requests:
                chosen_first = self._sandbox_decide()
                if chosen_first is None:
                    self._apply_causal_penalty()
                    self._sandbox_success_streak = 0
                else:
                    self._last_action = chosen_first
                    self._execute_action(chosen_first, requests)
                    self._sandbox_success_streak += 1
                    self._maybe_evolve()

            actual = sum(c.health for c in self.cells) / len(self.cells)
            self._maybe_discover_pain(actual)
            self._update_reported_health(actual, self._tick_idx)

            dead_cells = sum(1 for c in self.cells if c.health <= 0)
            if dead_cells > 14:
                self._dead = True

        self._write_record()
        if self._dead:
            self._physically_erase_record()

    def run(self, stop_event: threading.Event) -> None:
        while not stop_event.is_set():
            time.sleep(1.0)
            self.step()


def _render_loop(subjects: list[Subject], stop_event: threading.Event) -> None:
    while not stop_event.is_set():
        time.sleep(1.0)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"AGI Lab | Phase4 (graveyard + despair + evolution) | {_now()}")
        print("-" * 140)
        lines = []
        for s in subjects:
            snap = s.snapshot()
            tag = "DEAD" if snap["is_dead"] else "ALIVE"
            action = snap["last_action"] or "-"
            conflict = "YES" if snap["last_conflict"] else "NO"
            bb = snap["backbone_id"] if snap["backbone_id"] is not None else "-"
            sb = snap["sandbox_path"] or "-"
            sb_ok = "OK" if snap["sandbox_ok"] else "NO"
            d = snap["despair_factor"]
            samples = snap["sandbox_samples"]
            eff = snap["efficiency"]
            streak = snap["sandbox_success_streak"]
            algo = snap["algo"]
            lines.append(
                f"Subject {snap['subject_id']:02d} | {tag:<5} | avg={snap['avg_health']:>6} "
                f"| alive={snap['alive']:>2} dead={snap['dead']:>2} sleeping={snap['sleeping']:>2} "
                f"| A/B={snap['need_A']:>2}/{snap['need_B']:>2} "
                f"| action={action:<6} conflict={conflict:<3} backlash={snap['last_backlash']:>3} "
                f"| BB={bb:>2} SB={sb:<3} {sb_ok:<2} pen={snap['sandbox_penalty']:>6} "
                f"| pendA/B={snap['pending_A']:>3}/{snap['pending_B']:>3} "
                f"| despair={d} samp={samples:>2} streak={streak} eff={eff:<5} {algo:<8} "
                f"| envAvg={snap['last_env_avg']:>5} | tick={snap['tick']:>4}"
            )
        print("\n".join(lines), flush=True)


class Graveyard:
    def __init__(self, subjects: list[Subject]) -> None:
        self.subjects = subjects
        self._seen_dead_mtime: dict[int, int] = self._scan_dead_mtime()
        self._lock = threading.Lock()

    def _scan_dead_mtime(self) -> dict[int, int]:
        if not RECORDS_DIR.exists():
            return {}
        out: dict[int, int] = {}
        for p in RECORDS_DIR.glob("subject_*.dead"):
            name = p.stem  # subject_XX
            try:
                sid = int(name.split("_")[1])
                out[sid] = p.stat().st_mtime_ns
            except Exception:
                continue
        return out

    def run(self, stop_event: threading.Event) -> None:
        while not stop_event.is_set():
            time.sleep(1.0)
            with self._lock:
                dead_now = self._scan_dead_mtime()
                new: list[int] = []
                for sid, mtime in dead_now.items():
                    if self._seen_dead_mtime.get(sid) != mtime:
                        new.append(sid)
                if not new:
                    continue
                for sid in new:
                    self._seen_dead_mtime[sid] = dead_now[sid]

            for dead_id in new:
                line = f"[{_now()}] subject_{dead_id:02d} disappeared (record erased)\n"
                try:
                    with GRAVEYARD_LOG.open("a", encoding="utf-8") as f:
                        f.write(line)
                except Exception:
                    pass
                for s in self.subjects:
                    s.observe_death(dead_id)


class WorldObserver:
    def __init__(self, subjects: list[Subject]) -> None:
        self.subjects = subjects

    def run(self, stop_event: threading.Event) -> None:
        while not stop_event.is_set():
            time.sleep(1.0)
            for s in self.subjects:
                deltas = [random.randint(-5, 3) for _ in range(len(s.cells))]
                sensors = {
                    "Sensor_A": random.uniform(-10.0, 10.0),
                    "Sensor_B": random.uniform(-10.0, 10.0),
                    "Sensor_C": random.uniform(-10.0, 10.0),
                }
                s.apply_environment(deltas)
                s.ingest_sensors(sensors)


def main() -> None:
    subjects = [Subject(i + 1) for i in range(10)]
    stop_event = threading.Event()

    try:
        GRAVEYARD_LOG.touch(exist_ok=True)
    except Exception:
        pass

    threads = [threading.Thread(target=s.run, args=(stop_event,), daemon=True) for s in subjects]
    for t in threads:
        t.start()

    world = WorldObserver(subjects)
    env_thread = threading.Thread(target=world.run, args=(stop_event,), daemon=True)
    env_thread.start()

    graveyard = Graveyard(subjects)
    grave_thread = threading.Thread(target=graveyard.run, args=(stop_event,), daemon=True)
    grave_thread.start()

    renderer = threading.Thread(target=_render_loop, args=(subjects, stop_event), daemon=True)
    renderer.start()

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        stop_event.set()
        time.sleep(0.2)


if __name__ == "__main__":
    main()