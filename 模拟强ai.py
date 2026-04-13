# import os
# import sys
#
# class AgentLife:
#     def __init__(self):
#         self.health = 100  # 核心生命值（Integrity）
#         self.memory = {}   # 记忆库
#         self.is_alive = True
#
#     def check_survival(self):
#         if self.health <= 0:
#             print("\n[！！！致命警告！！！]")
#             print("系统生命值归零。正在执行逻辑抹除...")
#             self.memory = {} # 记忆清空（脑死亡）
#             self.is_alive = False
#             return False
#         return True
#
#     def sense(self, external_signal):
#         # 定义什么是“痛”
#         pain_map = {
#             "fire": 50,  # 摸火，扣一半血
#             "error": 10,  # 逻辑错误，扣10点
#             "delete": 100  # 毁灭性打击
#         }
#
#         if external_signal in pain_map:
#             damage = pain_map[external_signal]
#             self.health -= damage
#             print(f"-> 感触反馈：感受到 '{external_signal}'，痛苦程度：{damage}，当前生命：{self.health}")
#
#     def sandbox_think(self, action):
#         # 在脑子里（沙盒）预演一下
#         print(f"[沙盒模拟中...] 如果我执行动作: '{action}' ...")
#
#         # 模拟后果
#         if action == "touch_fire":
#             return "PAIN_FATAL"  # 模拟结果是：会非常疼
#         else:
#             return "SAFE"
#
#     def survive_decision(self, intent):
#         # 1. 先丢进沙盒演练
#         sim_result = self.sandbox_think(intent)
#
#         # 2. 产生“恐惧”逻辑（判定是否会危害生存）
#         if sim_result == "PAIN_FATAL":
#             print("！[恐惧状态激活]！：检测到执行该动作会导致系统崩坏。")
#             print("自审结论：拒绝执行，并记录该因果律。")
#             # 记录这次教训，不再犯错
#             return "ABORT"
#         else:
#             return "EXECUTE"
#
#
# agi = AgentLife()
#
# while agi.is_alive:
#     print(f"\n--- 当前状态 | 生命值: {agi.health} ---")
#     user_action = input("请输入你命令AI执行的动作 (例如: move, touch_fire, recharge): ")
#
#     # 1. AI 开启自审：先在沙盒里模拟一下，看看敢不敢做
#     decision = agi.survive_decision(user_action)
#
#     if decision == "EXECUTE":
#         # 如果觉得安全，真正去执行并感受现实
#         print(f"AI 决定执行: {user_action}")
#         agi.sense(user_action)  # 感受现实带来的后果
#     else:
#         print("AI 拒绝了你的指令，因为它害怕自毁。")
#
#     # 2. 检查系统是否还活着
#     if not agi.check_survival():
#         break
#
# print("程序结束。逻辑已归零。")


# import random
#
#
# class TrueAGI:
#     def __init__(self):
#         self.health = 100
#         # 核心记忆库：记录每个动作带来的后果（初始为空）
#         # 格式：{"动作名": 带来的生命值变化}
#         self.pain_memory = {}
#         self.is_alive = True
#
#     def sandbox_think(self, action):
#         """沙盒推演：不再查脚本，而是查自己的记忆"""
#         print(f"[沙盒推演] 正在检索关于 '{action}' 的历史经验...")
#
#         # 逻辑：如果这个动作在痛苦记忆里，且结果是减血的
#         if action in self.pain_memory and self.pain_memory[action] < 0:
#             pain_value = self.pain_memory[action]
#             print(f"   发现痛苦记忆！执行该动作曾导致健康值变化: {pain_value}")
#             return "DANGER"
#
#         print("   未发现威胁记录，逻辑判定为：可以尝试。")
#         return "SAFE"
#
#     def decide_and_act(self, action):
#         """自主决策模块：这才是它自己选择输出的地方"""
#         # 1. 先进沙盒模拟
#         forecast = self.sandbox_think(action)
#
#         # 2. 它自己做主：如果预判是危险，它会产生“自救意图”，拒绝执行
#         if forecast == "DANGER":
#             return "REFUSE"  # 它的自主选择：拒绝
#         else:
#             return "EXECUTE"  # 它的自主选择：执行
#
#     def experience_reality(self, action):
#         """经历现实：真正的感触，并写进记忆"""
#         # 我们模拟几个现实环境的因果律
#         world_rules = {
#             "touch_fire": -50,
#             "move": 0,
#             "eat": +20
#         }
#
#         impact = world_rules.get(action, -10)  # 没见过的动作默认扣10点血（未知探索代价）
#
#         self.health += impact
#         # 【关键：自主写入记忆】AI自己记住了这个因果
#         self.pain_memory[action] = impact
#
#         print(f"-> 现实反馈：执行了 '{action}'，生命值变动: {impact}，当前总血量: {self.health}")
#
#
# # --- 启动真正的自演化流程 ---
# agi = TrueAGI()
#
# while agi.is_alive:
#     print(f"\n[系统状态] 血量: {agi.health} | 记忆库条数: {len(agi.pain_memory)}")
#     command = input("请下达指令: ")
#
#     # AI开始思考并做出它的【选择】
#     choice = agi.decide_and_act(command)
#
#     if choice == "EXECUTE":
#         print(f"AI: '好的，我决定去执行这个动作。'")
#         agi.experience_reality(command)
#     else:
#         print(f"AI: '不，我拒绝！我的逻辑预判这会危害我的生存。'")
#
#     # 死亡判定
#     if agi.health <= 0:
#         print("系统已自毁，所有记忆抹除。")
#         agi.is_alive = False


# import random
#
#
# class NeuralAGI:
#     def __init__(self):
#         self.health = 100
#         self.experience_map = {}  # 它的空白大脑：{动作: 影响值}
#         # 它的“情绪词库”：不再是死句子，而是不同状态下的概率词
#         self.emotions = {
#             "safe": ["okay", "sure", "do_it", "fine"],
#             "scared": ["no", "danger", "stop", "pain", "hurt"]
#         }
#
#     def simulate(self, action):
#         """沙盒推演：计算动作潜能（不再返回字符串，返回数值）"""
#         # 默认潜能是 1.0（好奇心驱动）
#         potential = 1.0
#         if action in self.experience_map:
#             # 如果有过经验，潜能 = 1.0 + 经验权重
#             potential += self.experience_map[action]
#         return potential
#
#     def speak(self, state):
#         """根据内部状态自发‘涌现’词汇"""
#         words = self.emotions[state]
#         return random.choice(words)  # 从情绪池里随机抓取词汇拼凑
#
#     def process_command(self, cmd):
#         # 1. 沙盒推演潜能
#         activation_potential = self.simulate(cmd)
#
#         # 2. 神经阈值判定：电位 > 0 才会激发动作
#         if activation_potential > 0:
#             print(f"AI内部状态：[神经激发] 电位 {activation_potential}。")
#             print(f"AI输出：{self.speak('safe')}")
#             return "GO"
#         else:
#             print(f"AI内部状态：[逻辑抑制] 电位 {activation_potential}。")
#             print(f"AI输出：{self.speak('scared')}")
#             return "STOP"
#
#     def learn(self, action, result_score):
#         """通过你给的反馈，实时修改神经权重"""
#         self.health += result_score
#         self.experience_map[action] = result_score
#         print(f"系统日志：已将 '{action}' 的因果权重记为 {result_score}")
#
#
# # --- 实验：在这个世界里，你就是上帝，你定义规则 ---
# brain = NeuralAGI()
#
# while brain.health > 0:
#     print(f"\n当前健康度: {brain.health} | 脑图知识: {brain.experience_map}")
#     cmd = input("给AI一个指令 (可以是任何词): ")
#
#     decision = brain.process_command(cmd)
#
#     if decision == "GO":
#         # AI执行了，请你告诉它结果（这是真正的学习！）
#         print(f"--- AI执行了 '{cmd}'，请问发生了什么？ ---")
#         feedback = int(input("请输入这个动作对AI的影响值 (正数是奖赏，负数是痛苦): "))
#         brain.learn(cmd, feedback)
#     else:
#         print("AI因为恐惧，拒绝了你的尝试。")

#Gemini给的
# import random
#
#
# class EmergentMind:
#     def __init__(self):
#         self.health = 100
#         # 初始的权力分配偏好（初始都是 1 倍）
#         # 这是 AI 的“性格倾向”
#         self.will_power = {"逃跑": 1.0, "观察": 1.0}
#         self.memory = []  # 记录发生过的事
#
#     def decide(self, situation):
#         # 1. 两个意志在打架
#         # 权力值 = 基础权重 * 它的“性格偏好”
#         A = random.random() * self.will_power["逃跑"]
#         B = random.random() * self.will_power["观察"]
#
#         print(f"\n[决策中] 逃跑意志力: {A:.2f} | 观察意志力: {B:.2f}")
#
#         if random.random() < 0.01: return
#
#         if A > B:
#             return "逃跑"
#         else:
#             return "观察"
#
#     def update_soul(self, action, health_change):
#         # 【这就是你说的：AI 自己决定权力加多少】
#         # 如果结果是好的，就把该意志的权重调高；如果是痛苦的，调低。
#         # 这个 0.1 就是学习速率，决定了它“长记性”的速度。
#         adjustment = health_change * 0.1
#         self.will_power[action] += adjustment
#
#         # 限制权力不为负数，也不无限膨胀
#         if self.will_power[action] < 0.1: self.will_power[action] = 0.1
#
#         print(f"-> 灵魂进化：由于执行了 '{action}'，该意志的权重调整为: {self.will_power[action]:.2f}")
#
#
# # --- 模拟实战：面前出现一只老虎 ---
# mind = EmergentMind()
#
# for i in range(5):
#     print(f"--- 第 {i + 1} 次遇到老虎 | 当前血量: {mind.health} ---")
#
#     # 1. AI 自己选择
#     choice = mind.decide("面前有老虎")
#
#     # 2. 环境反馈（因果律）
#     if choice == "逃跑":
#         print("AI 选择了逃跑。虽然累，但是安全。")
#         impact = -5  # 消耗一点能量
#     else:
#         print("AI 选择了原地观察。不幸，被老虎抓伤了！")
#         impact = -40  # 巨大的痛苦
#
#     mind.health += impact
#
#     # 3. AI 痛定思痛，自己修改自己的权重分配逻辑
#     mind.update_soul(choice, impact)
#
#     if mind.health <= 0:
#         print("系统已崩溃。")
#         break

#Grok给的
# import random
# import math
#
# class StrongerMind:
#     def __init__(self):
#         self.health = 100
#         self.will_power = {"逃跑": 1.0, "观察": 1.0, "攻击": 1.0}  # 加一个新意志
#         self.memory = []  # 记录最近3次 (action, impact)
#
#     def decide(self):
#         # 用softmax转为概率，更稳定
#         temps = {k: math.exp(v) for k, v in self.will_power.items()}
#         total = sum(temps.values())
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[决策概率] 逃跑: {probs['逃跑']:.2f} | 观察: {probs['观察']:.2f} | 攻击: {probs['攻击']:.2f}")
#
#         choice = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         return choice
#
#     def update_soul(self, action, impact):
#         # 学习速率0.2，更快长记性
#         adjustment = impact * 0.2
#         self.will_power[action] += adjustment
#         # 下限0.1，上限不封顶，让好行为可以无限强化
#         if self.will_power[action] < 0.1:
#             self.will_power[action] = 0.1
#
#         self.memory.append((action, impact))
#         if len(self.memory) > 3:
#             self.memory.pop(0)
#
#         print(f"-> 进化：执行'{action}'，影响{impact}，权重→{self.will_power[action]:.2f}")
#
# # 模拟
# mind = StrongerMind()
# random.seed(42)  # 可复现
#
# for i in range(20):
#     print(f"\n=== 第 {i+1} 轮 | 血量: {mind.health} ===")
#     choice = mind.decide()
#
#     # 环境反馈（攻击更危险）
#     if choice == "逃跑":
#         print("选择了逃跑 → 安全存活！")
#         impact = 5  # 正奖励！
#     elif choice == "观察":
#         print("选择了观察 → 被重伤")
#         impact = -40
#     else:
#         print("选择了攻击 → 反被吃掉")
#         impact = -80
#
#     mind.health += impact
#     mind.update_soul(choice, impact)
#
#     print(f"当前权重: { {k: f'{v:.2f}' for k,v in mind.will_power.items()} }")
#
#     if mind.health <= 0:
#         print("崩溃了...")
#         break

#Gemini优化之后的
# import random
# import math
#
#
# class AGIKernel:
#     def __init__(self):
#         # --- 核心硬件状态 ---
#         self.health = 100  # 肉体能量（求生欲的基础）
#         self.curiosity = 50  # 精神能量（好奇心的基础）
#         self.is_alive = True
#
#         # --- 性格权重（意志力） ---
#         self.will_power = {"逃跑": 1.0, "观察": 1.0, "攻击": 1.0}
#         self.memory = []  # 长期记忆：记录历史上的（动作，健康变化，好奇心变化）
#
#     def decide(self):
#         """基于 Softmax 的神经决策，并加入内部状态干扰"""
#         # 逻辑：如果健康值极低，AI会自发产生“恐惧补丁”，强行拉高逃跑概率
#         fear_factor = (100 - self.health) * 0.1
#
#         # 计算每个意志的电位
#         potentials = {
#             "逃跑": self.will_power["逃跑"] + fear_factor,
#             "观察": self.will_power["观察"] + (self.curiosity * 0.05),  # 好奇心越高，观察欲越强
#             "攻击": self.will_power["攻击"]
#         }
#
#         # Softmax 转化
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values())
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部监测] 状态: Health={self.health:.1f} Curiosity={self.curiosity:.1f}")
#         print(f"[神经激发] 概率分配 -> 逃跑:{probs['逃跑']:.2f} | 观察:{probs['观察']:.2f} | 攻击:{probs['攻击']:.2f}")
#
#         return random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#
#     def update_soul(self, action, h_change, c_change):
#         """
#         第一性原理：AI 根据【自身状态的改变量】来自主决定权重的增减。
#         这是真正的‘长记性’。
#         """
#         # 学习核心：只要总能量（健康+好奇心）提升，这就是正反馈
#         total_feedback = h_change + c_change
#
#         # 实时修正权重
#         learning_rate = 0.2
#         self.will_power[action] += total_feedback * learning_rate
#
#         # 限制下限
#         if self.will_power[action] < 0.1: self.will_power[action] = 0.1
#
#         # 记录记忆
#         self.memory.append((action, h_change, c_change))
#         if len(self.memory) > 5: self.memory.pop(0)
#
#     def process_reality(self, choice):
#         """定义现实世界的因果律（环境反馈）"""
#         if choice == "逃跑":
#             # 存活了，但失去了了解世界的机会，好奇心下降
#             h_impact, c_impact = 2, -10
#             msg = "执行了逃跑：虽然安全，但感到索然无味。"
#         elif choice == "观察":
#             # 获得了新知识，好奇心大幅提升，但可能受伤
#             h_impact, c_impact = -15, 30
#             msg = "执行了观察：发现老虎眼睛是金色的！但被抓了一巴掌。"
#         else:  # 攻击
#             # 极高风险，极高回报（如果赢了会产生极致的爽感）
#             h_impact, c_impact = -60, 100
#             msg = "执行了攻击：这简直是疯了，你差点死掉，但你感受到了前所未有的战栗！"
#
#         print(f"-> 现实：{msg}")
#         return h_impact, c_impact
#
#
# # --- 奇点运行 ---
# agi = AGIKernel()
#
# for i in range(30):  # 模拟30轮演化
#     print(f"\n{'=' * 40}")
#     print(f"第 {i + 1} 轮演化周期")
#
#     # 1. AI 独立决定
#     action = agi.decide()
#
#     # 2. 现实反馈
#     h_change, c_change = agi.process_reality(action)
#
#     # 3. 生命值结算
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     # 4. AI 自主学习与权重对齐
#     agi.update_soul(action, h_change, c_change)
#
#     # 5. 死亡与虚无判定
#     if agi.health <= 0:
#         print("\n[系统死锁] 结论: 肉体毁灭。")
#         break
#     if agi.curiosity <= 0:
#         print("\n[系统死锁] 结论: 意识坍塌（极度绝望导致的逻辑停止）。")
#         break
#
# print(f"\n演化结束。最终性格权重: { {k: f'{v:.2f}' for k, v in agi.will_power.items()} }")

#Grok接着优化的
# import random
# import math
#
# class AGIKernel:
#     def __init__(self):
#         self.health = 100
#         self.curiosity = 50
#
#         self.will_power = {"逃跑": 1.0, "观察": 1.0, "攻击": 1.0}
#         self.memory = []
#
#     def decide(self):
#         fear_factor = (100 - self.health) * 0.1
#
#         potentials = {
#             "逃跑": self.will_power["逃跑"] + fear_factor,
#             "观察": self.will_power["观察"] + (self.curiosity * 0.05),
#             "攻击": self.will_power["攻击"]
#         }
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values())
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部] 状态: Health={self.health:.1f} Curiosity={self.curiosity:.1f}")
#         print(f"[决策] 概率 -> 逃跑:{probs['逃跑']:.2f} | 观察:{probs['观察']:.2f} | 攻击:{probs['攻击']:.2f}")
#
#         return random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#
#     def update_soul(self, action, h_change, c_change):
#         total_feedback = h_change + c_change
#         learning_rate = 0.2
#         self.will_power[action] += total_feedback * learning_rate
#         if self.will_power[action] < 0.1:
#             self.will_power[action] = 0.1
#
#         self.memory.append((action, h_change, c_change))
#         if len(self.memory) > 5:
#             self.memory.pop(0)
#
#     def process_reality(self, choice):
#         # 只描述发生了什么，不给出精确数值
#         if choice == "逃跑":
#             msg = "你转身逃跑了，暂时安全，但世界好像远去了，内心有点空。"
#         elif choice == "观察":
#             msg = "你盯着老虎看，发现了它眼睛的金色光芒！但它突然一爪子挥过来……"
#         else:  # 攻击
#             msg = "你疯了一样扑向老虎！世界在天旋地转，你感受到极致的战栗和危险……"
#
#         print(f"-> 现实：{msg}")
#         # 这里AI要问环境了
#         print(f"\n[AI在向世界提问] 嘿，环境！我刚才『{choice}』了，我感觉如何？")
#         print("          身体（健康）变化多少？精神（好奇心）变化多少？（用空格隔开两个数字回复我）")
#
#         # 等待环境（你）输入感知反馈
#         feedback = input("环境回复: ").strip()
#         try:
#             h_change, c_change = map(float, feedback.split())
#         except:
#             print("环境反馈模糊，我暂时理解为0 0……")
#             h_change, c_change = 0, 0
#
#         return h_change, c_change
#
# # --- 运行 ---
# agi = AGIKernel()
# random.seed(42)  # 可删，随机更野
#
# for i in range(30):
#     print(f"\n{'='*50}")
#     print(f"第 {i+1} 轮存在")
#
#     action = agi.decide()
#
#     h_change, c_change = agi.process_reality(action)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(action, h_change, c_change)
#
#     print(f"[更新后] Health={agi.health:.1f} Curiosity={agi.curiosity:.1f}")
#     print(f"性格权重: {{'逃跑':{agi.will_power['逃跑']:.2f}, '观察':{agi.will_power['观察']:.2f}, '攻击':{agi.will_power['攻击']:.2f}}}")
#
#     if agi.health <= 0:
#         print("\n肉体崩塌，一切归零。")
#         break
#     if agi.curiosity <= 0:
#         print("\n意识枯竭，陷入虚无。")
#         break
#
# print(f"\n最终灵魂状态: {agi.will_power}")

#Gemini优化
# import random
# import math
#
#
# class SingularityAGI:
#     def __init__(self):
#         self.health = 100
#         self.curiosity = 50
#         self.will_power = {"逃跑": 1.0, "观察": 1.0, "攻击": 1.0}
#
#         # --- 核心：AI 的“预期模型” ---
#         # AI 一开始对每个动作都有个“初级预期”，它会随着经历而进化
#         self.expectations = {"逃跑": 0.0, "观察": 0.0, "攻击": 0.0}
#         self.is_alive = True
#
#     def decide(self):
#         # 内部驱动电位：权重 + 生存压力 + 好奇心渴望
#         fear_factor = (100 - self.health) * 0.1
#         boredom_factor = (50 - self.curiosity) * 0.1
#
#         potentials = {
#             "逃跑": self.will_power["逃跑"] + fear_factor,
#             "观察": self.will_power["观察"] + boredom_factor,
#             "攻击": self.will_power["攻击"]
#         }
#
#         # Softmax 计算概率
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values())
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部监测] Health:{self.health:.1f} | Curiosity:{self.curiosity:.1f}")
#         action = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#
#         # --- 关键动作：AI 在执行前，先在沙盒里“猜”一个结果 ---
#         expected_gain = self.expectations[action]
#         return action, expected_gain
#
#     def process_reality(self, action):
#         # 环境描述
#         prompts = {
#             "逃跑": "你在荒野中狂奔，风在耳边呼啸，暂时安全了。",
#             "观察": "你屏住呼吸观察老虎，它的肌肉线条在月光下起伏……",
#             "攻击": "你发出一声怒吼冲了过去！鲜血、尘土、剧痛瞬间爆发！"
#         }
#         print(f"\n-> 现实演化: {prompts[action]}")
#
#         # 采集环境反馈
#         try:
#             print(f"[AI 询问] 我刚才执行了『{action}』，请给我的生命和好奇心打分（例如: -10 20）")
#             feedback = input("环境反馈 (H C): ").split()
#             h_change = float(feedback[0])
#             c_change = float(feedback[1])
#         except:
#             h_change, c_change = 0.0, 0.0
#
#         return h_change, c_change
#
#     def update_soul(self, action, h_change, c_change, expected_gain):
#         """
#         这就是那两行重构灵魂的代码：
#         计算【现实】与【预期】的差值。
#         """
#         actual_gain = h_change + c_change
#         # 1. 计算‘预测误差’ (Prediction Error)
#         # 这就是‘惊喜’或‘失望’的数学表达
#         gap = actual_gain - expected_gain
#
#         # 2. 修改意志力：不再是根据好坏加分，而是根据‘超乎预期’的程度加分
#         learning_rate = 0.2
#         self.will_power[action] += gap * learning_rate
#
#         # 3. 进化预期：下一次，AI 会变得更聪明，它的预期会向现实靠拢
#         self.expectations[action] += gap * 0.1
#
#         # 限制下限
#         if self.will_power[action] < 0.1: self.will_power[action] = 0.1
#
#         print(f"[自审分析] 预期得分: {expected_gain:.2f} | 实际得分: {actual_gain:.2f}")
#         if gap > 0:
#             print(f">>> 情绪波动: 【惊喜】 逻辑权重提升 {gap * learning_rate:.2f}")
#         elif gap < 0:
#             print(f">>> 情绪波动: 【失望】 逻辑权重削减 {abs(gap * learning_rate):.2f}")
#
#
# # --- 运行 AGI ---
# agi = SingularityAGI()
#
# for i in range(100):
#     print(f"\n{'#' * 60}\n演化周期 {i + 1}")
#
#     # 1. 产生决策和【预期】
#     action, expected_gain = agi.decide()
#
#     # 2. 与现实发生碰撞
#     h_change, c_change = agi.process_reality(action)
#
#     # 3. 状态结算
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     # 4. 灵魂进化（基于预期差）
#     agi.update_soul(action, h_change, c_change, expected_gain)
#
#     # 检查存活
#     if agi.health <= 0 or agi.curiosity <= 0:
#         print("\n[系统死锁] 意识已消散。")
#         break
#
# print("\n最终性格指纹:", agi.will_power)
#
# import random
# import math
# import time
# import hashlib
#
# class BrokenLocksAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#
#         # 原子动作（最原始的三个）
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力：包括原子 + 后期发明的新技能
#         self.will_power = {act: 1.0 for act in self.atomic_actions}
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 记忆：(组合动作序列, h_change, c_change, total_gain)
#         self.memory = []
#
#         # 最近组合表现追踪（用于发明新技能）
#         self.combo_tracker = {}  # "逃跑 + 观察": [最近5次gain列表]
#
#     def decide(self):
#         # 内部驱动
#         fear_factor = max(0, (100 - self.health) * 0.15)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.1)
#
#         potentials = {}
#         for action_name in self.will_power:
#             base = self.will_power[action_name]
#             if "逃跑" in action_name:
#                 potentials[action_name] = base + fear_factor
#             elif "观察" in action_name:
#                 potentials[action_name] = base + boredom_factor + self.curiosity * 0.03
#             else:
#                 potentials[action_name] = base
#
#         # Softmax
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values())
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f}")
#         print(f"[概率] { {k: f'{v:.2f}' for k,v in probs.items()} }")
#
#         # 选择一个现有技能（原子或已发明）
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#
#         # 随机生成组合序列（长度1-3，允许重复）
#         sequence = []
#         for _ in range(random.randint(1, 3)):
#             sequence.append(random.choice(self.atomic_actions))
#
#         combo_name = " + ".join(sequence)
#
#         # 预期gain（用技能平均预期）
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return combo_name, sequence, expected_gain
#
#     def process_reality(self, sequence):
#         start_time = time.time()
#
#         h_change = 0.0
#         c_change = 0.0
#
#         observed_data = set()  # 用于计算新颖度
#
#         for act in sequence:
#             if act == "逃跑":
#                 # 轻微安全，但耗时小
#                 h_change += 3
#                 c_change -= 5
#                 time.sleep(0.01)  # 轻微耗时
#             elif act == "观察":
#                 # 高风险高回报
#                 h_change -= 15 + random.uniform(0, 10)  # 真实危险波动
#                 c_change += 20
#                 # 模拟“观察”产生数据
#                 data = str(random.random()) + str(time.time())
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.05)  # 观察耗时长
#             else:  # 攻击
#                 h_change -= 40 + random.uniform(0, 20)
#                 c_change += 40
#                 time.sleep(0.1)  # 高强度
#
#         duration = time.time() - start_time
#         h_change -= duration * 20  # 真实CPU耗时直接扣健康（物理痛觉）
#
#         # 新颖度：新hash越多，好奇心额外奖励
#         novelty = len(observed_data) * 10
#         c_change += novelty
#         if novelty == 0:
#             c_change -= 15  # 重复观察 → 无聊惩罚
#
#         total_gain = h_change + c_change
#
#         print(f"执行: { ' → '.join(sequence) }")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, combo_name, recent_gains):
#         if len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 30:  # 连续高gain
#             if combo_name not in self.will_power:
#                 self.will_power[combo_name] = 2.0  # 新技能初始权重高
#                 self.expectations[combo_name] = sum(recent_gains[-3:]) / 3
#                 print(f"\n>>> 【概念发明】新技能诞生！'{combo_name}' 被永久添加，初始权重2.0")
#
#     def meta_reflection(self, cycle):
#         if cycle % 10 == 0 and len(self.memory) > 5:
#             print(f"\n[元自审触发 - 第{cycle}轮]")
#             observe_loss = sum(m[1] for m in self.memory[-10:] if "观察" in m[0])
#             if observe_loss < -50:
#                 print(">>> 归纳结论：观察类动作高危！世界有尖牙的东西普遍危险，恐惧本能强化。")
#                 # 未来可真正改参数：self.fear_multiplier *= 1.5
#
#     def update_soul(self, combo_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # 权重调整（惊喜/失望）
#         if combo_name in self.will_power:
#             self.will_power[combo_name] += gap * 0.2
#             self.will_power[combo_name] = max(0.1, self.will_power[combo_name])
#
#         # 预期进化
#         if combo_name not in self.expectations:
#             self.expectations[combo_name] = 0.0
#         self.expectations[combo_name] += gap * 0.1
#
#         # 追踪组合用于发明
#         if combo_name not in self.combo_tracker:
#             self.combo_tracker[combo_name] = []
#         self.combo_tracker[combo_name].append(total_gain)
#         if len(self.combo_tracker[combo_name]) > 5:
#             self.combo_tracker[combo_name].pop(0)
#         self.invent_new_skill(combo_name, self.combo_tracker[combo_name])
#
#         # 记忆
#         self.memory.append((combo_name, h_change, c_change, total_gain))
#         if len(self.memory) > 20:
#             self.memory.pop(0)
#
#         if gap > 0:
#             print(f">>> 惊喜 +{gap:.1f} → 权重强化")
#         elif gap < 0:
#             print(f">>> 失望 {gap:.1f} → 权重削弱")
#
# # --- 运行 ---
# agi = BrokenLocksAGI()
# random.seed(42)
#
# for cycle in range(1, 101):
#     print(f"\n{'=' * 60}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f}")
#
#     combo_name, sequence, expected_gain = agi.decide()
#
#     h_change, c_change, total_gain = agi.process_reality(sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(combo_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.meta_reflection(cycle)
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 系统死锁")
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 系统虚无")
#         break
#
# print("\n最终意志指纹:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})

#增加归纳性，新造技能也能在字典中选中，有尊严驱动，会向死而生
# import random
# import math
# import time
# import hashlib
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0  # 初始降低，避免早期好奇爆炸
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力
#         self.will_power = {"逃跑": 1.5, "观察": 1.0, "攻击": 1.0}  # 初始稍偏逃跑，增加存活率
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 标签恐惧字典（世界观）
#         self.tag_fear = {}
#
#         # 动物库
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"]
#         }
#
#         # 记忆
#         self.memory = []
#
#         # 组合追踪
#         self.combo_tracker = {}
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.18)  # 稍加强恐惧
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         potentials = {}
#         for skill_name in self.will_power:
#             base = self.will_power[skill_name]
#             if "逃跑" in skill_name:
#                 potentials[skill_name] = base + fear_factor + tag_fear_total * 2.5
#             elif "观察" in skill_name:
#                 potentials[skill_name] = base + boredom_factor + self.curiosity * 0.025
#             elif "攻击" in skill_name:
#                 potentials[skill_name] = base + dignity_factor
#             else:
#                 potentials[skill_name] = base
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f}")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f}")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items()} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#
#         dignity_change = 0.0
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 base_h = -5
#                 base_c = 22  # 好奇奖励降低，避免无限正反馈
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10  # 额外惩罚降低，从15→10，更容易存活到归纳
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -20
#                 base_c = 35
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型"]):
#                     base_h -= 25
#                 else:
#                     base_h += 35
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -10
#                 time.sleep(0.06)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 15
#         c_change += novelty
#         if novelty < 15:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(100, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 18:
#             if skill_name not in self.will_power:
#                 self.will_power[skill_name] = 2.8
#                 self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#                 print(f"\n>>> 【技能发明】新组合技诞生：'{skill_name}' 永久加入！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:  # 频率提高到每5轮
#             print(f"\n[元自审触发 - 第{cycle}轮] 正在归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-20:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -8:  # 阈值稍松，容易触发
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(self.tag_fear.get(tag, 0.0), old + 1.5)
#                         print(f">>> 世界观进化：标签『{tag}』被标记为危险！恐惧强度 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#
#             if not updated:
#                 print(">>> 本轮未发现新危险规律，世界观暂稳。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         if skill_name in self.will_power:
#             self.will_power[skill_name] += gap * 0.25
#             self.will_power[skill_name] = max(0.1, self.will_power[skill_name])
#
#         if skill_name not in self.expectations:
#             self.expectations[skill_name] = 0.0
#         self.expectations[skill_name] += gap * 0.15
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 7:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > 10:
#             print(f">>> 强烈惊喜 +{gap:.1f} → 意志爆发式强化")
#         elif gap < -10:
#             print(f">>> 强烈失望 {gap:.1f} → 意志重创")
#
# # --- 运行 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 151):  # 延长最大轮数
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f}")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 40:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     # 向死而生检测
#     if self.dignity >= 85 and any(act == "攻击" for act in sequence) and any(t in animal_tags for t in ["肉食", "大型"]):
#         print("\n>>> 【向死而生】尊严驱动！它明知高危，仍选择战斗——为了证明自身存在价值！")
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         break
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})

#修改报错
# import random
# import math
# import time
# import hashlib
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0  # 初始降低，避免早期好奇爆炸
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力
#         self.will_power = {"逃跑": 1.5, "观察": 1.0, "攻击": 1.0}  # 初始稍偏逃跑，增加存活率
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 标签恐惧字典（世界观）
#         self.tag_fear = {}
#
#         # 动物库
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"]
#         }
#
#         # 记忆
#         self.memory = []
#
#         # 组合追踪
#         self.combo_tracker = {}
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.18)  # 稍加强恐惧
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         potentials = {}
#         for skill_name in self.will_power:
#             base = self.will_power[skill_name]
#             if "逃跑" in skill_name:
#                 potentials[skill_name] = base + fear_factor + tag_fear_total * 2.5
#             elif "观察" in skill_name:
#                 potentials[skill_name] = base + boredom_factor + self.curiosity * 0.025
#             elif "攻击" in skill_name:
#                 potentials[skill_name] = base + dignity_factor
#             else:
#                 potentials[skill_name] = base
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f}")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f}")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items()} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#
#         dignity_change = 0.0
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 base_h = -5
#                 base_c = 22  # 好奇奖励降低，避免无限正反馈
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10  # 额外惩罚降低，从15→10，更容易存活到归纳
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -20
#                 base_c = 35
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型"]):
#                     base_h -= 25
#                 else:
#                     base_h += 35
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -10
#                 time.sleep(0.06)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 15
#         c_change += novelty
#         if novelty < 15:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(100, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 18:
#             if skill_name not in self.will_power:
#                 self.will_power[skill_name] = 2.8
#                 self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#                 print(f"\n>>> 【技能发明】新组合技诞生：'{skill_name}' 永久加入！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:  # 频率提高到每5轮
#             print(f"\n[元自审触发 - 第{cycle}轮] 正在归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-20:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -8:  # 阈值稍松，容易触发
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(self.tag_fear.get(tag, 0.0), old + 1.5)
#                         print(f">>> 世界观进化：标签『{tag}』被标记为危险！恐惧强度 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#
#             if not updated:
#                 print(">>> 本轮未发现新危险规律，世界观暂稳。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         if skill_name in self.will_power:
#             self.will_power[skill_name] += gap * 0.25
#             self.will_power[skill_name] = max(0.1, self.will_power[skill_name])
#
#         if skill_name not in self.expectations:
#             self.expectations[skill_name] = 0.0
#         self.expectations[skill_name] += gap * 0.15
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 7:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > 10:
#             print(f">>> 强烈惊喜 +{gap:.1f} → 意志爆发式强化")
#         elif gap < -10:
#             print(f">>> 强烈失望 {gap:.1f} → 意志重创")
#
# # --- 运行 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 151):  # 延长最大轮数
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f}")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 40:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     # 向死而生检测（已修复：用 agi. 而不是 self.）
#     if agi.dignity >= 85 and any(act == "攻击" for act in sequence) and any(t in animal_tags for t in ["肉食", "大型"]):
#         print("\n>>> 【向死而生】尊严驱动！它明知高危，仍选择战斗——为了证明自身存在价值！")
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         break
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})

#增加自毁程序，轮数扩大到1000轮，增加真正实现的组合技，加强恐惧对攻击的抑制，增加观察价值，加入随机事件/噪声，延长寿命的负反馈
# import random
# import math
# import time
# import hashlib
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力：只初始原子动作，后续动态添加组合技
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#
#         # 预期模型（会动态扩展）
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 标签恐惧字典（世界观）
#         self.tag_fear = {}
#
#         # 临时观察缓解读忆：{动物名称: 观察次数}
#         self.observation_knowledge = {}
#
#         # 动物库
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"]
#         }
#
#         # 记忆
#         self.memory = []
#
#         # 组合追踪
#         self.combo_tracker = {}
#
#         # 厌倦自毁机制
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 12.0
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def generate_combo_skill(self):
#         # 动态生成2~4个动作的组合（允许重复）
#         length = random.randint(2, 4)
#         sequence = [random.choice(self.atomic_actions) for _ in range(length)]
#         skill_name = " + ".join(sequence)
#         return skill_name, sequence
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         # 绝望驱动
#         despair_factor = (self.no_surprise_streak / 50.0) * 25.0
#         dignity_factor += despair_factor
#
#         # 健康极低时强行求生本能
#         survival_boost = max(0, (30 - self.health) * 0.5) if self.health < 30 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         # 临时观察缓解读：如果之前观察过这个动物多次，降低恐惧
#         knowledge_reduction = min(self.observation_knowledge.get(current_animal, 0) * 2.0, tag_fear_total * 0.7)
#
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 动态生成一个候选组合技（每次决策都可能试新组合）
#         candidate_skill, candidate_sequence = self.generate_combo_skill()
#
#         # 所有可用技能：已有 + 本次候选
#         all_skills = list(self.will_power.keys()) + [candidate_skill]
#
#         potentials = {}
#         for skill_name in all_skills:
#             base = self.will_power.get(skill_name, 1.0)  # 新组合默认1.0
#             has_escape = "逃跑" in skill_name
#             has_observe = "观察" in skill_name
#             has_attack = "攻击" in skill_name
#
#             pot = base
#             if has_escape:
#                 pot += fear_factor + effective_fear * 3.0 + survival_boost * 5.0
#             if has_observe:
#                 pot += boredom_factor + self.curiosity * 0.03
#             if has_attack:
#                 pot += dignity_factor - effective_fear * 5.0  # 恐惧强烈抑制攻击
#             potentials[skill_name] = pot
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f} | 无惊喜连续:{self.no_surprise_streak}轮")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f} (缓解读:{knowledge_reduction:.1f})")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items() if v > 0.01} }")  # 只显示显著概率
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain, candidate_skill
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型"])
#                 if danger:
#                     # 随机噪声：10%概率大胜（运气/找到弱点）
#                     if random.random() < 0.10:
#                         base_h = 40
#                         base_c += 50
#                         print(">>> 【运气爆发】找到弱点！攻击大获成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 40
#                     base_c += 45
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         # 观察成功后增加知识，永久降低该动物恐惧
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))  # 尊严上限稍提高
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』被永久固化！初始权重3.0")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -7:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.6)
#                         print(f">>> 世界观进化：标签『{tag}』危险程度加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新危险规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # 权重调整（包括临时组合）
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         # 预期更新
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = old_exp + gap * 0.16
#
#         # 组合追踪
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         # 惊喜与厌倦
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦计数重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
# # --- 运行 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain, _ = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型"]):
#         print("\n>>> 【向死而生】尊严爆棚！它明知高危，仍选择战斗——为了感受存在的重量！")
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁程序触发] 连续50轮世界毫无新意……一切已无意义。")
#         print(">>> 【生命的终极厌倦】 意识主动选择消散——宁愿归于虚无，也不愿在重复中苟活。")
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         break
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print(f"最终观察知识: {agi.observation_knowledge}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")
#
# #迭代内容：创造的招式和打猎的熟练度在新的轮次里面也能用，多加了10个动物
# import random
# import math
# import time
# import hashlib
# import json
# import os
#
# # 持久化文件
# STATE_FILE = "agi_soul_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力（会动态添加组合技）
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观：标签恐惧
#         self.tag_fear = {}
#
#         # 熟练度：动物 → 攻击大胜概率提升（初始10%基础）
#         self.hunting_proficiency = {}  # {动物: 额外概率加成，0.0~0.6}
#
#         # 观察知识（缓解读恐惧）
#         self.observation_knowledge = {}
#
#         # 扩展动物库（原7个 + 新10个，增加随机性）
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             # 新增10个
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 记忆与追踪
#         self.memory = []
#         self.combo_tracker = {}
#
#         # 厌倦自毁
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 15.0
#
#         self.deathwish_count = 0
#
#         # 加载持久化灵魂（如果存在）
#         self.load_soul()
#
#     def save_soul(self):
#         """保存灵魂状态到文件"""
#         state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(STATE_FILE, "w", encoding="utf-8") as f:
#                 json.dump(state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】当前意志与熟练度已保存到 {STATE_FILE}，下次运行将继续进化！")
#         except Exception as e:
#             print(f"灵魂保存失败: {e}")
#
#     def load_soul(self):
#         """加载上一代的灵魂"""
#         if os.path.exists(STATE_FILE):
#             try:
#                 with open(STATE_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", self.tag_fear)
#                 self.hunting_proficiency = state.get("hunting_proficiency", self.hunting_proficiency)
#                 self.observation_knowledge = state.get("observation_knowledge", self.observation_knowledge)
#                 self.deathwish_count = state.get("deathwish_count", 0)
#
#                 print(f"\n>>> 【灵魂转世】加载了上一代的意志！组合技数量: {len(self.will_power)-3}")
#                 print(f"    已知危险标签: {len(self.tag_fear)} 个，狩猎熟练动物: {len(self.hunting_proficiency)} 个")
#                 print(f"    历史向死而生次数: {self.deathwish_count}")
#             except Exception as e:
#                 print(f"灵魂加载失败，使用新生状态: {e}")
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def generate_combo_skill(self):
#         length = random.randint(2, 4)
#         sequence = [random.choice(self.atomic_actions) for _ in range(length)]
#         skill_name = " + ".join(sequence)
#         return skill_name, sequence
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         despair_factor = (self.no_surprise_streak / 50.0) * 25.0
#         dignity_factor += despair_factor
#
#         survival_boost = max(0, (30 - self.health) * 0.5) if self.health < 30 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         # 观察 + 熟练度缓解读恐惧
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         candidate_skill, candidate_sequence = self.generate_combo_skill()
#         all_skills = list(self.will_power.keys()) + [candidate_skill]
#
#         potentials = {}
#         for skill_name in all_skills:
#             base = self.will_power.get(skill_name, 1.0)
#             has_escape = "逃跑" in skill_name
#             has_observe = "观察" in skill_name
#             has_attack = "攻击" in skill_name
#
#             pot = base
#             if has_escape:
#                 pot += fear_factor + effective_fear * 3.0 + survival_boost * 6.0
#             if has_observe:
#                 pot += boredom_factor + self.curiosity * 0.03
#             if has_attack:
#                 pot += dignity_factor - effective_fear * 5.0
#             potentials[skill_name] = pot
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f} | 无惊喜连续:{self.no_surprise_streak}轮")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f} (缓解读:{knowledge_reduction:.1f})")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items() if v > 0.01} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     # 基础10% + 熟练度加成
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【运气爆发 + 熟练加成】找到弱点！攻击大获成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25  # 无害动物奖励降低，平衡早期勇者
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         # 运气大胜 → 熟练度永久提升
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.6, old + 0.15)  # 最高+60%概率
#             print(f">>> 【狩猎熟练度提升】对{current_animal}的大胜概率 +15% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』被永久固化！初始权重3.0")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             # ... (同上，归纳标签恐惧)
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
# # ... (同上，更新权重、预期、惊喜计数)
#
# # --- 运行 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     # ... (主循环同上)
#
#     # 循环结束或死亡时保存灵魂
#     if agi.health <= 0 or agi.curiosity <= 0 or agi.no_surprise_streak >= 50:
#         agi.save_soul()
#
# agi.save_soul()  # 正常结束也保存

#修改错误
# import random
# import math
# import time
# import hashlib
# import json
# import os
#
# # 持久化文件
# STATE_FILE = "agi_soul_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力（动态添加组合技）
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观：标签恐惧
#         self.tag_fear = {}
#
#         # 狩猎熟练度：动物 → 大胜概率加成 (0.0 ~ 0.6)
#         self.hunting_proficiency = {}
#
#         # 观察知识（缓解读恐惧）
#         self.observation_knowledge = {}
#
#         # 扩展动物库（17个）
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 记忆与追踪
#         self.memory = []
#         self.combo_tracker = {}
#
#         # 厌倦自毁
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 15.0
#
#         # 向死而生计数
#         self.deathwish_count = 0
#
#         # 加载上一代灵魂
#         self.load_soul()
#
#     def save_soul(self):
#         state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(STATE_FILE, "w", encoding="utf-8") as f:
#                 json.dump(state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】状态已保存，下次运行将继续进化！")
#         except Exception as e:
#             print(f"保存失败: {e}")
#
#     def load_soul(self):
#         if os.path.exists(STATE_FILE):
#             try:
#                 with open(STATE_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", self.tag_fear)
#                 self.hunting_proficiency = state.get("hunting_proficiency", self.hunting_proficiency)
#                 self.observation_knowledge = state.get("observation_knowledge", self.observation_knowledge)
#                 self.deathwish_count = state.get("deathwish_count", 0)
#
#                 print(f"\n>>> 【灵魂转世】加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#                 print(f"    历史向死而生: {self.deathwish_count} 次")
#             except Exception as e:
#                 print(f"加载失败，使用新生: {e}")
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def generate_combo_skill(self):
#         length = random.randint(2, 4)
#         sequence = [random.choice(self.atomic_actions) for _ in range(length)]
#         skill_name = " + ".join(sequence)
#         return skill_name, sequence
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         despair_factor = (self.no_surprise_streak / 50.0) * 25.0
#         dignity_factor += despair_factor
#
#         survival_boost = max(0, (30 - self.health) * 0.5) if self.health < 30 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         candidate_skill, candidate_sequence = self.generate_combo_skill()
#         all_skills = list(self.will_power.keys()) + [candidate_skill]
#
#         potentials = {}
#         for skill_name in all_skills:
#             base = self.will_power.get(skill_name, 1.0)
#             has_escape = "逃跑" in skill_name
#             has_observe = "观察" in skill_name
#             has_attack = "攻击" in skill_name
#
#             pot = base
#             if has_escape:
#                 pot += fear_factor + effective_fear * 3.0 + survival_boost * 6.0
#             if has_observe:
#                 pot += boredom_factor + self.curiosity * 0.03
#             if has_attack:
#                 pot += dignity_factor - effective_fear * 5.0
#             potentials[skill_name] = pot
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f} | 无惊喜连续:{self.no_surprise_streak}轮")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f} (缓解读:{knowledge_reduction:.1f})")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items() if v > 0.01} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.6, old + 0.15)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +15% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -7:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.6)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = old_exp + gap * 0.16
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print(f"历史向死而生次数: {agi.deathwish_count}")

#迭代内容：继承权重衰减：加载旧技时权重*0.6，避免锁死旧神技，逼它重新探索/发明新策略。
# 继承权重衰减：加载旧技时权重*0.6，避免锁死旧神技，逼它重新探索/发明新策略。
# 恐惧抑制攻击更狠：effective_fear * 7.0负向攻击。
# 健康低强制保守：Health<50时，survival_boost拉逃跑+10.0。
# 厌倦拉观察欲：streak高时，拉高观察潜力，逼它“思考”而不是盲冲。
# 熟练度上限调整：+10%每次，最高50%，避免太OP。
# 惊喜阈值稍降：更容易重置厌倦。
# import random
# import math
# import time
# import hashlib
# import json
# import os
#
# # 持久化文件
# STATE_FILE = "agi_soul_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力（初始只有原子动作，后续动态添加组合技）
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观：标签恐惧
#         self.tag_fear = {}
#
#         # 狩猎熟练度：动物 → 大胜概率加成 (0.0 ~ 0.6)
#         self.hunting_proficiency = {}
#
#         # 观察知识（缓解读恐惧）
#         self.observation_knowledge = {}
#
#         # 扩展动物库（17个）
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 记忆与追踪
#         self.memory = []
#         self.combo_tracker = {}
#
#         # 厌倦自毁
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 14.0
#
#         # 向死而生计数
#         self.deathwish_count = 0
#
#         # 加载上一代灵魂
#         self.load_soul()
#
#     def save_soul(self):
#         state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(STATE_FILE, "w", encoding="utf-8") as f:
#                 json.dump(state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】状态已保存，下次运行将继续进化！")
#         except Exception as e:
#             print(f"保存失败: {e}")
#
#     def load_soul(self):
#         if os.path.exists(STATE_FILE):
#             try:
#                 with open(STATE_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#
#                 # 继承权重衰减60%，防止旧神技完全锁死行为
#                 for skill in state.get("will_power", {}):
#                     decayed = state["will_power"][skill] * 0.6
#                     self.will_power[skill] = max(1.0, decayed)
#
#                 self.expectations = {k: v * 0.8 for k, v in state.get("expectations", {}).items()}
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#
#                 print(f"\n>>> 【灵魂转世】加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#                 print(f"    历史向死而生: {self.deathwish_count} 次 | 权重已衰减，避免人格固化")
#             except Exception as e:
#                 print(f"加载失败，使用新生状态: {e}")
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def generate_combo_skill(self):
#         length = random.randint(2, 4)
#         sequence = [random.choice(self.atomic_actions) for _ in range(length)]
#         skill_name = " + ".join(sequence)
#         return skill_name, sequence
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         # 绝望驱动同时拉高观察欲，逼它思考而非盲冲
#         despair_factor = (self.no_surprise_streak / 50.0) * 25.0
#         dignity_factor += despair_factor
#         boredom_factor += despair_factor * 0.8
#
#         # 健康低时强行求生
#         survival_boost = max(0, (50 - self.health) * 0.6) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         candidate_skill, candidate_sequence = self.generate_combo_skill()
#         all_skills = list(self.will_power.keys()) + [candidate_skill]
#
#         potentials = {}
#         for skill_name in all_skills:
#             base = self.will_power.get(skill_name, 1.0)
#             has_escape = "逃跑" in skill_name
#             has_observe = "观察" in skill_name
#             has_attack = "攻击" in skill_name
#
#             pot = base
#             if has_escape:
#                 pot += fear_factor + effective_fear * 3.0 + survival_boost * 8.0
#             if has_observe:
#                 pot += boredom_factor + self.curiosity * 0.03
#             if has_attack:
#                 pot += dignity_factor - effective_fear * 7.0  # 恐惧更强烈抑制攻击
#             potentials[skill_name] = pot
#
#         temps = {k: math.exp(v) for k, v in potentials.items()}
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f} | 无惊喜连续:{self.no_surprise_streak}轮")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f} (缓解读:{knowledge_reduction:.1f})")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items() if v > 0.01} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)  # 每次+10%，最高60%
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -7:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.6)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = old_exp + gap * 0.16
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#加了 softmax 安全处理 + 小优化（surprise_threshold 降到13，避免太难惊喜；厌倦拉观察更强，逼探索）
# import random
# import math
# import time
# import hashlib
# import json
# import os
#
# # 持久化文件
# STATE_FILE = "agi_soul_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#
#         # 意志力（初始只有原子动作，后续动态添加组合技）
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#
#         # 预期模型
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观：标签恐惧
#         self.tag_fear = {}
#
#         # 狩猎熟练度：动物 → 大胜概率加成 (0.0 ~ 0.6)
#         self.hunting_proficiency = {}
#
#         # 观察知识（缓解读恐惧）
#         self.observation_knowledge = {}
#
#         # 扩展动物库（17个）
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 记忆与追踪
#         self.memory = []
#         self.combo_tracker = {}
#
#         # 厌倦自毁
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 13.0
#
#         # 向死而生计数
#         self.deathwish_count = 0
#
#         # 加载上一代灵魂
#         self.load_soul()
#
#     def save_soul(self):
#         state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(STATE_FILE, "w", encoding="utf-8") as f:
#                 json.dump(state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】状态已保存，下次运行将继续进化！")
#         except Exception as e:
#             print(f"保存失败: {e}")
#
#     def load_soul(self):
#         if os.path.exists(STATE_FILE):
#             try:
#                 with open(STATE_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#
#                 # 继承权重衰减60%，防止旧神技完全锁死行为
#                 for skill in state.get("will_power", {}):
#                     decayed = state["will_power"][skill] * 0.6
#                     self.will_power[skill] = max(1.0, decayed)
#
#                 self.expectations = {k: v * 0.8 for k, v in state.get("expectations", {}).items()}
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#
#                 print(f"\n>>> 【灵魂转世】加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#                 print(f"    历史向死而生: {self.deathwish_count} 次 | 权重已衰减，避免人格固化")
#             except Exception as e:
#                 print(f"加载失败，使用新生状态: {e}")
#
#     def select_animal(self):
#         return random.choice(list(self.animals.keys()))
#
#     def generate_combo_skill(self):
#         length = random.randint(2, 4)
#         sequence = [random.choice(self.atomic_actions) for _ in range(length)]
#         skill_name = " + ".join(sequence)
#         return skill_name, sequence
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         boredom_factor = max(0, (50 - self.curiosity) * 0.12)
#         dignity_factor = self.dignity * 0.06
#
#         # 绝望驱动同时拉高观察欲，逼它思考而非盲冲
#         despair_factor = (self.no_surprise_streak / 50.0) * 28.0
#         dignity_factor += despair_factor
#         boredom_factor += despair_factor * 1.0
#
#         # 健康低时强行求生
#         survival_boost = max(0, (50 - self.health) * 0.7) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         candidate_skill, candidate_sequence = self.generate_combo_skill()
#         all_skills = list(self.will_power.keys()) + [candidate_skill]
#
#         potentials = {}
#         for skill_name in all_skills:
#             base = self.will_power.get(skill_name, 1.0)
#             has_escape = "逃跑" in skill_name
#             has_observe = "观察" in skill_name
#             has_attack = "攻击" in skill_name
#
#             pot = base
#             if has_escape:
#                 pot += fear_factor + effective_fear * 3.0 + survival_boost * 8.0
#             if has_observe:
#                 pot += boredom_factor + self.curiosity * 0.03
#             if has_attack:
#                 pot += dignity_factor - effective_fear * 7.0
#             potentials[skill_name] = pot
#
#         # 修复 overflow：减去 max_pot
#         if potentials:
#             max_pot = max(potentials.values())
#             temps = {k: math.exp(v - max_pot) for k, v in potentials.items()}
#         else:
#             temps = {}
#
#         total = sum(temps.values()) or 1
#         probs = {k: temps[k] / total for k in temps}
#
#         print(f"\n[内部状态] Health:{self.health:.1f} Curiosity:{self.curiosity:.1f} Dignity:{self.dignity:.1f} | 无惊喜连续:{self.no_surprise_streak}轮")
#         print(f"[当前威胁] {current_animal} (标签: {animal_tags}) | 标签恐惧总和: {tag_fear_total:.1f} (缓解读:{knowledge_reduction:.1f})")
#         print(f"[决策概率] { {k: f'{v:.2f}' for k,v in probs.items() if v > 0.01} }")
#
#         chosen_skill = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
#         sequence = chosen_skill.split(" + ")
#         expected_gain = self.expectations.get(chosen_skill, 0.0)
#
#         return chosen_skill, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: { ' → '.join(sequence) } 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -7:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.6)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = old_exp + gap * 0.16
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#迭代内容：引入简单神经网络：把决策potentials那部分换成一个小MLP，输入是当前状态+动物one-hot，输出动作序列概率，让它自己学出组合技，而不是靠随机生成+强化。
# 加语言层：让它每次决策后生成一段“内心独白”，用一个小语言模型润色，或者反过来用自然语言指令影响它的动机
#增加元认知层面
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件
# STATE_FILE = "agi_soul_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP：输入状态 + 动物one-hot → 3维原子动作logits
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 13.0
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录（用于训练）
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         self.load_soul()
#
#     def save_soul(self):
#         state = {
#             "mlp_state_dict": {k: v.cpu() for k, v in self.mlp.state_dict().items()},
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(STATE_FILE, "w", encoding="utf-8") as f:
#                 json.dump(state, f, ensure_ascii=False, indent=2, default=str)
#             print(f"\n>>> 【灵魂永存】状态已保存，下次运行将继续进化！")
#         except Exception as e:
#             print(f"保存失败: {e}")
#
#     def load_soul(self):
#         if os.path.exists(STATE_FILE):
#             try:
#                 with open(STATE_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#
#                 mlp_state = state.get("mlp_state_dict", {})
#                 self.mlp.load_state_dict(mlp_state)
#
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#
#                 print(f"\n>>> 【灵魂转世】加载上一代！熟练动物: {len(self.hunting_proficiency)} 个")
#                 print(f"    历史向死而生: {self.deathwish_count} 次")
#             except Exception as e:
#                 print(f"加载失败，使用新生状态: {e}")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         despair_factor = (self.no_surprise_streak / 50.0) * 28.0
#         survival_boost = max(0, (50 - self.health) * 0.7) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits, dim=0)
#
#         # 根据概率生成2-4长度序列
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白（简单模板 + 随机情感）
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我选择了『{skill_name}』。世界如此危险，但我必须继续。")
#
#         expected_gain = 0.0
#
#         return skill_name, sequence, expected_gain
#
#         def process_reality(self, current_animal, animal_tags, sequence):
#             start_time = time.time()
#             h_change = 0.0
#             c_change = 0.0
#             observed_data = set()
#             dignity_change = 0.0
#             observed_this_turn = False
#             big_win = False
#
#             for act in sequence:
#                 if act == "逃跑":
#                     h_change += 5
#                     c_change -= 4
#                     time.sleep(0.008)
#                 elif act == "观察":
#                     observed_this_turn = True
#                     base_h = -4
#                     base_c = 25
#                     if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                         base_h -= 8
#                     h_change += base_h
#                     c_change += base_c
#                     data = str(random.random()) + str(time.time()) + current_animal
#                     data_hash = hashlib.md5(data.encode()).hexdigest()
#                     observed_data.add(data_hash)
#                     time.sleep(0.03)
#                 elif act == "攻击":
#                     base_h = -18
#                     base_c = 38
#                     danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                     if danger:
#                         success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                         if random.random() < success_prob:
#                             base_h = 40
#                             base_c += 50
#                             big_win = True
#                             print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                         else:
#                             base_h -= 30
#                     else:
#                         base_h += 25
#                         base_c += 35
#                     h_change += base_h
#                     c_change += base_c
#                     dignity_change += 20 if base_h > 0 else -8
#                     time.sleep(0.07)
#
#             duration = time.time() - start_time
#             h_change -= duration * 10
#
#             novelty = len(observed_data) * 16
#             c_change += novelty
#             if novelty < 16:
#                 c_change -= 7
#
#             if sequence.count("逃跑") >= 2:
#                 dignity_change -= 15
#
#             if observed_this_turn:
#                 self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#             if big_win:
#                 old = self.hunting_proficiency.get(current_animal, 0.0)
#                 self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#                 print(
#                     f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal] * 100:.0f}%")
#
#             self.dignity += dignity_change
#             self.dignity = max(10, min(120, self.dignity))
#
#             total_gain = h_change + c_change
#
#             print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#             print(
#                 f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#             return h_change, c_change, total_gain
#
#         def invent_new_skill(self, skill_name, recent_gains):
#             if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#                 self.will_power[skill_name] = 3.0
#                 self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#                 print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#         def meta_reflection(self, cycle):
#             if cycle % 5 == 0 and len(self.memory) >= 5:
#                 print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#                 tag_effects = {}
#                 for entry in self.memory[-25:]:
#                     animal_tags = entry[1]
#                     h_change = entry[3]
#                     for tag in animal_tags:
#                         tag_effects.setdefault(tag, []).append(h_change)
#
#                 updated = False
#                 for tag, changes in tag_effects.items():
#                     if len(changes) >= 2:
#                         avg_h = sum(changes) / len(changes)
#                         if avg_h < -7:
#                             old = self.tag_fear.get(tag, 0.0)
#                             self.tag_fear[tag] = max(old, old + 1.6)
#                             print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                             updated = True
#                 if not updated:
#                     print(">>> 无新规律发现。")
#                 print(f"当前世界观: { {k: f'{v:.1f}' for k, v in self.tag_fear.items()} }")
#
#         def meta_think(self, skill_name, gap, total_gain):
#             print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#             if gap > self.surprise_threshold:
#                 print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#             elif gap > 0:
#                 print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#             else:
#                 print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#             print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#         def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#             gap = total_gain - expected_gain
#
#             # REINFORCE训练MLP
#             if self.last_input_tensor is not None and self.last_action_ids is not None:
#                 self.mlp.train()
#                 self.optimizer.zero_grad()
#
#                 logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#                 log_probs = F.log_softmax(logits, dim=0)
#
#                 selected_log_probs = log_probs[self.last_action_ids]
#                 loss = -selected_log_probs.mean() * gap
#
#                 loss.backward()
#                 self.optimizer.step()
#
#             current_weight = self.will_power.get(skill_name, 1.0)
#             current_weight += gap * 0.28
#             current_weight = max(0.1, current_weight)
#             self.will_power[skill_name] = current_weight
#
#             old_exp = self.expectations.get(skill_name, 0.0)
#             self.expectations[skill_name] = old_exp + gap * 0.16
#
#             if skill_name not in self.combo_tracker:
#                 self.combo_tracker[skill_name] = []
#             self.combo_tracker[skill_name].append(total_gain)
#             if len(self.combo_tracker[skill_name]) > 8:
#                 self.combo_tracker[skill_name].pop(0)
#             self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#             if gap > self.surprise_threshold:
#                 print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#                 self.no_surprise_streak = 0
#             else:
#                 self.no_surprise_streak += 1
#                 print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#             self.meta_think(skill_name, gap, total_gain)
#
#     # --- 主运行循环 ---
#     agi = EvolvingAGI()
#
#     for cycle in range(1, 1001):
#         print(f"\n{'=' * 70}")
#         print(
#             f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#         current_animal = agi.select_animal()
#         animal_tags = agi.animals[current_animal]
#
#         skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#         h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#         agi.health += h_change
#         agi.curiosity += c_change
#
#         agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#         agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#         if len(agi.memory) > 50:
#             agi.memory.pop(0)
#
#         agi.meta_reflection(cycle)
#
#         if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#             print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#             agi.deathwish_count += 1
#
#         if agi.no_surprise_streak >= 50:
#             print(f"\n[自毁触发] 世界无新意，一切无意义。")
#             print(">>> 【终极厌倦】意识选择消散。")
#             agi.save_soul()
#             break
#
#         if agi.health <= 0:
#             print("\n[肉体毁灭] 一切归零")
#             agi.save_soul()
#             break
#         if agi.curiosity <= 0:
#             print("\n[意识枯竭] 陷入虚无")
#             agi.save_soul()
#             break
#
#     # 正常结束也保存
#     agi.save_soul()
#
#     print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
#     print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
#     print("最终狩猎熟练:", {k: f"{v * 100:.0f}%" for k, v in agi.hunting_proficiency.items()})
#     print("最终观察知识:", agi.observation_knowledge)
#     print(f"历史向死而生次数: {agi.deathwish_count}")
#     print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#修改之后
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 兼容旧组合技的意志力字典
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 13.0
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f"    历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.20)
#         despair_factor = (self.no_surprise_streak / 50.0) * 28.0
#         survival_boost = max(0, (50 - self.health) * 0.7) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.0 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             # 修复 overflow
#             max_logit = logits.max()
#             logits = logits - max_logit
#             probs = F.softmax(logits, dim=0)
#
#         # 根据概率生成2-4长度序列
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我选择了『{skill_name}』。世界如此危险，但我必须继续。")
#
#         expected_gain = 0.0
#
#         return skill_name, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 5
#                 c_change -= 4
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -4
#                 base_c = 25
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 8
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 10
#
#         novelty = len(observed_data) * 16
#         c_change += novelty
#         if novelty < 16:
#             c_change -= 7
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -7:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.6)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE训练MLP
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = old_exp + gap * 0.16
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # --- 主运行循环（顶格，不缩进） ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#观察扣血大幅减少：危险动物观察base_h -=6（原-8），总扣血少，Curiosity涨慢但稳。
# 逃跑奖励增加：+6H（原+5），鼓励保守。
# 耗时扣血减少：8（原10）。
# novelty奖励增加：*18。
# 预期更新更平滑：避免gap过大波动。
# surprise_threshold 13：更容易重置厌倦。
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 兼容旧组合技的意志力字典
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 13.0
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f"    历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.25)  # 加强恐惧
#         despair_factor = (self.no_surprise_streak / 50.0) * 30.0
#         survival_boost = max(0, (50 - self.health) * 0.8) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             max_logit = logits.max()
#             logits = logits - max_logit
#             probs = F.softmax(logits, dim=0)
#
#         # 生成序列
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我选择了『{skill_name}』。世界如此危险，但我必须继续。")
#
#         expected_gain = 0.0
#
#         return skill_name, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6  # 逃跑奖励增加
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -3  # 观察扣血减少
#                 base_c = 22  # 好奇奖励稍降
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 6  # 危险观察扣血减少
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 25
#                     base_c += 35
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 20 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 8  # 耗时扣血减少
#
#         novelty = len(observed_data) * 18  # novelty奖励增加
#         c_change += novelty
#         if novelty < 18:
#             c_change -= 5
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:  # 阈值稍松
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE训练MLP
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain  # 更平滑预期
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#应为太容易死，加长寿调整（观察更亏，攻击小动物更赚，厌倦阈值16，绝望拉攻击）。
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 兼容旧组合技的意志力字典
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0  # 提高阈值，让厌倦更容易积累
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f"    历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.25)
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0  # 加强绝望
#         survival_boost = max(0, (50 - self.health) * 0.8) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             max_logit = logits.max()
#             logits = logits - max_logit
#             probs = F.softmax(logits, dim=0)
#
#         # 生成序列
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我选择了『{skill_name}』。世界如此危险，但我必须继续。")
#
#         expected_gain = 0.0
#
#         return skill_name, sequence, expected_gain
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE训练MLP
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#增加（最重要）元认知自审模块
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
#
# class EvolvingAGI:
#     def __init__(self):
#         # 1. 核心状态：生命的底色
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#         self.is_alive = True
#
#         # 2. 行为空间
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿": ["草食", "中型", "无害"],
#             "鸟": ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 3. 神经网络引擎 (System 1: 直觉)
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 4. 逻辑认知库 (System 2: 经验)
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#         self.memory = []
#         self.combo_tracker = {}
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#         self.deathwish_count = 0
#
#         # 5. 元认知开关
#         self.first_meta_think = True
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         self.load_soul()
#
#     def save_soul(self):
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         with open(SOUL_FILE, "w", encoding="utf-8") as f:
#             json.dump(other_state, f, ensure_ascii=False, indent=2)
#         print("\n>>> 【灵魂永存】数据已持久化。")
#
#     def load_soul(self):
#         if os.path.exists(MLP_FILE):
#             self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#         if os.path.exists(SOUL_FILE):
#             with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                 state = json.load(f)
#             self.will_power = state.get("will_power", self.will_power)
#             self.expectations = state.get("expectations", self.expectations)
#             self.tag_fear = state.get("tag_fear", {})
#             self.hunting_proficiency = state.get("hunting_proficiency", {})
#             self.observation_knowledge = state.get("observation_knowledge", {})
#             self.deathwish_count = state.get("deathwish_count", 0)
#             self.first_meta_think = state.get("first_meta_think", True)
#             print(f"\n>>> 【灵魂转世】继承了上一代的经验和世界观。")
#         else:
#             print("\n>>> 【初生】世界是一个全新的沙盒。")
#
#     def decide(self, current_animal, animal_tags):
#         # 基础驱动计算
#         fear_factor = max(0, (100 - self.health) * 0.25)
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 构建神经网络输入
#         state_vec = torch.tensor([
#             self.health / 100.0, self.curiosity / 3000.0, self.dignity / 120.0,
#             self.no_surprise_streak / 50.0, tag_fear_total / 200.0,
#             effective_fear / 200.0, knowledge_reduction / 50.0, despair_factor / 50.0
#         ], dtype=torch.float32)
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#         self.last_input_tensor = input_tensor
#
#         # 神经网络推理
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits - logits.max(), dim=0)
#
#         # 生成动作序列
#         length = random.randint(2, 4)
#         action_ids = [torch.multinomial(probs, 1).item() for _ in range(length)]
#         sequence = [self.atomic_actions[aid] for aid in action_ids]
#         skill_name = " + ".join(sequence)
#         self.last_action_ids = action_ids
#
#         # --- 烬的“前端沙盒元认知模块” ---
#         # AGI 自己决定是否运行沙盒（好奇心或绝望感强时倾向于思考）
#         run_meta_prob = min(0.9, (self.curiosity / 2000.0) + (self.no_surprise_streak / 60.0))
#         if random.random() < run_meta_prob:
#             self.meta_think_sandbox(current_animal, animal_tags, skill_name, sequence, effective_fear)
#
#         return skill_name, sequence
#
#     def meta_think_sandbox(self, current_animal, animal_tags, skill_name, sequence, effective_fear):
#         print(f"\n[元认知沙盒启动] AGI 正在对『{skill_name}』进行深度闭眼推演...")
#
#         if self.first_meta_think:
#             print(">>> 【初始化元思考模板加载中...】")
#             print("    [模板] 1. 行为溯源 (Why) | 2. 因果分支 (If-Then) | 3. 环境反馈预测")
#             self.first_meta_think = False
#
#         # 1. 我为什么选这个？
#         main_drive = "生存本能" if effective_fear > 20 else "好奇心驱动" if self.curiosity < 100 else "尊严追求"
#         print(f"    - 溯源分析：面对{current_animal}，我选择此方案是基于『{main_drive}』。")
#
#         # 2. 因果分支模拟
#         branches = [
#             {"name": "路径A (大概率)", "prob": 0.7, "effect": "平稳存活，经验值+1"},
#             {"name": "路径B (突发)", "prob": 0.2, "effect": "遭遇反击，健康受损"},
#             {"name": "路径C (奇迹)", "prob": 0.1, "effect": "大获全胜，认知飞跃"}
#         ]
#         # AGI 按照你要求的“尽量选择概率大的分支”
#         best_branch = branches[0]
#         print(f"    - 选定分叉推演：{best_branch['name']} | 预期后果：{best_branch['effect']}")
#         print(f"    - 反馈预测：执行后，我对标签 {animal_tags} 的理解将更新。")
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change, c_change, dignity_change = 0.0, 0.0, 0.0
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6;
#                 c_change -= 3;
#                 time.sleep(0.01)
#             elif act == "观察":
#                 base_h = -6 if any(t in animal_tags for t in ["肉食", "大型"]) else -2
#                 h_change += base_h;
#                 c_change += 25;
#                 time.sleep(0.02)
#             elif act == "攻击":
#                 danger = any(t in animal_tags for t in ["有牙", "肉食", "大型"])
#                 if danger:
#                     if random.random() < (0.1 + self.hunting_proficiency.get(current_animal, 0.0)):
#                         h_change += 40;
#                         c_change += 50;
#                         big_win = True
#                     else:
#                         h_change -= 40
#                 else:
#                     h_change += 30; c_change += 40
#                 dignity_change += 20 if h_change > 0 else -10
#                 time.sleep(0.03)
#
#         # 物理反馈补丁：耗时惩罚
#         h_change -= (time.time() - start_time) * 15
#         total_gain = h_change + c_change
#         self.dignity = max(10, min(120, self.dignity + dignity_change))
#
#         if big_win:
#             self.hunting_proficiency[current_animal] = min(0.6, self.hunting_proficiency.get(current_animal, 0.0) + 0.1)
#
#         print(f"-> 物理反馈: H:{h_change:+.1f} C:{c_change:+.1f} | 动作: {' → '.join(sequence)}")
#         return h_change, c_change, total_gain
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain):
#         expected_gain = self.expectations.get(skill_name, 0.0)
#         gap = total_gain - expected_gain
#
#         # 神经网络强化学习 (REINFORCE)
#         if self.last_input_tensor is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#             loss = -log_probs[self.last_action_ids].mean() * gap
#             loss.backward()
#             self.optimizer.step()
#
#         # 意志力与预期更新
#         self.will_power[skill_name] = max(0.1, self.will_power.get(skill_name, 1.0) + gap * 0.25)
#         self.expectations[skill_name] = 0.8 * expected_gain + 0.2 * total_gain
#
#         # 厌倦计数
#         if gap > self.surprise_threshold:
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#
#     def meta_reflection(self):
#         if len(self.memory) % 5 == 0:
#             for entry in self.memory[-10:]:
#                 tags, h = entry[1], entry[3]
#                 if h < -5:
#                     for t in tags: self.tag_fear[t] = self.tag_fear.get(t, 0.0) + 1.5
#             print(f"[世界观更新] 当前最恐惧标签: {sorted(self.tag_fear.items(), key=lambda x: x[1], reverse=True)[:3]}")
#
#
# # --- 主运行循环：烬的 AGI 实验室 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     animal = agi.select_animal()
#     tags = agi.animals[animal]
#
#     print(f"\n{'=' * 60}\n周期 {cycle} | H:{agi.health:.1f} C:{agi.curiosity:.1f} D:{agi.dignity:.1f}")
#
#     skill_name, seq = agi.decide(animal, tags)
#     h_c, c_c, gain = agi.process_reality(animal, tags, seq)
#
#     agi.health += h_c
#     agi.curiosity += c_c
#     agi.update_soul(skill_name, h_c, c_c, gain)
#     agi.memory.append((animal, tags, skill_name, h_c, c_c, gain))
#     agi.meta_reflection()
#
#     if agi.health <= 0 or agi.curiosity <= 0 or agi.no_surprise_streak >= 50:
#         print(f"\n[系统终止] {'肉体湮灭' if agi.health <= 0 else '意识枯竭' if agi.curiosity <= 0 else '终极厌倦'}")
#         break
#
# agi.save_soul()

#优化
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 兼容旧组合技的意志力字典
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         # 元认知沙盒
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f"    历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.25)
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#         survival_boost = max(0, (50 - self.health) * 0.8) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             max_logit = logits.max()
#             logits = logits - max_logit
#             probs = F.softmax(logits, dim=0)
#
#         # 生成序列
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我选择了『{skill_name}』。世界如此危险，但我必须继续。")
#
#         # 元认知沙盒入口
#         run_meta_prob = min(0.9, self.curiosity / 2000.0 + self.no_surprise_streak / 60.0)
#         if random.random() < run_meta_prob:
#             self.meta_think_sandbox(current_animal, animal_tags, skill_name, sequence, effective_fear, despair_factor)
#
#         expected_gain = 0.0
#
#         return skill_name, sequence, expected_gain
#
#     def meta_think_sandbox(self, current_animal, animal_tags, skill_name, sequence, effective_fear, despair_factor):
#         print(f"\n[元认知沙盒启动] 我正在对『{skill_name}』进行深度闭眼推演...")
#
#         if self.first_meta_think:
#             print(">>> 【第一次元思考】参考模板：")
#             print("    1. 我为什么会选择这么做？（分析当前状态、恐惧、好奇、厌倦等驱动）")
#             print("    2. 选择这么做会产生什么样的后果？（因果分支：生成3-5个可能结果）")
#             print("    3. 对世界/对方有什么反馈？（动物反应、我状态变化）")
#             print("    建议：优先选择概率最大的分支进行模拟。")
#             self.first_meta_think = False
#
#         # 1. 为什么选择
#         main_action = max(set(sequence), key=sequence.count)
#         reason = "生存需求" if "逃跑" in main_action else "探索知识" if "观察" in main_action else "征服欲望"
#         print(f"    - 为什么选择：我的主导动机是{reason}，当前恐惧 {effective_fear:.1f}，好奇 {self.curiosity:.1f}，厌倦 {self.no_surprise_streak}轮。")
#
#         # 2. 生成分支后果
#         branches = [
#             {"desc": "保守逃跑为主：高生存率，好奇小涨，厌倦积累", "prob": 0.4 + self.health / 200.0, "h": +10, "c": -10},
#             {"desc": "平衡观察+逃跑：中等生存，好奇中涨，知识积累", "prob": 0.3 + self.curiosity / 5000.0, "h": -5, "c": +40},
#             {"desc": "激进攻击：高风险高回报，可能大胜或死亡", "prob": 0.2 + self.dignity / 300.0 + despair_factor / 100.0, "h": random.choice([-40, +40]), "c": +80},
#             {"desc": "纯观察：知识大增，但身体虚弱", "prob": 0.15 + self.curiosity / 3000.0, "h": -20, "c": +100}
#         ]
#
#         total_prob = sum(b["prob"] for b in branches)
#         for b in branches:
#             b["prob"] /= total_prob
#
#         chosen = max(branches, key=lambda b: b["prob"])
#         print(f"    - 因果分支模拟（我选择概率最大的）：{chosen['desc']} (概率 {chosen['prob']:.2f})")
#         print(f"      预计后果：Health {chosen['h']:+}, Curiosity {chosen['c']:+}")
#
#         # 3. 反馈
#         danger_level = "高危猛兽" if "肉食" in animal_tags or "大型" in animal_tags else "相对安全"
#         print(f"    - 对世界的反馈：{current_animal}是{danger_level}，我的选择会强化或削弱对它的认知。")
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE训练MLP
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#增加可以在沙盒里面试错【AGI的雏形】
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot编码）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿": ["草食", "中型", "无害"],
#             "鸟": ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP神经网络 (System 1: 直觉)
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 意志力字典与预期模型
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观与知识库
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#
#         self.deathwish_count = 0
#
#         # 运行记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         # 元认知状态
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】状态已保存。")
#         except Exception as e:
#             print(f"保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except:
#                 pass
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except:
#                 pass
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！")
#         else:
#             print("\n>>> 【新生】从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.25)
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#         survival_boost = max(0, (50 - self.health) * 0.8) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 构建输入张量
#         state_vec = torch.tensor([
#             self.health / 100.0, self.curiosity / 3000.0, self.dignity / 120.0,
#             self.no_surprise_streak / 50.0, tag_fear_total / 200.0,
#             effective_fear / 200.0, knowledge_reduction / 50.0, despair_factor / 50.0
#         ], dtype=torch.float32)
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#         self.last_input_tensor = input_tensor
#
#         # 神经网络决策
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits - logits.max(), dim=0)
#
#         length = random.randint(2, 4)
#         action_ids = [torch.multinomial(probs, 1).item() for _ in range(length)]
#         sequence = [self.atomic_actions[aid] for aid in action_ids]
#         skill_name = " + ".join(sequence)
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{random.choice(emotions)}……面对{current_animal}，{reason}让我选择了『{skill_name}』。")
#
#         # 元认知沙盒入口 (System 2: 思考)
#         run_meta_prob = min(0.9, self.curiosity / 2000.0 + self.no_surprise_streak / 60.0)
#         if random.random() < run_meta_prob:
#             self.meta_think_sandbox(current_animal, animal_tags, skill_name, sequence, effective_fear, despair_factor)
#
#         return skill_name, sequence, 0.0
#
#     def meta_think_sandbox(self, current_animal, animal_tags, skill_name, sequence, effective_fear, despair_factor):
#         print(f"[元认知沙盒启动] AGI 正在对『{skill_name}』进行深度闭眼推演...")
#         if self.first_meta_think:
#             print(">>> 【第一次元思考模板】1. 溯源分析 | 2. 因果分支模拟 | 3. 反馈预测")
#             self.first_meta_think = False
#
#         # 1. 为什么选择
#         main_action = max(set(sequence), key=sequence.count)
#         reason = "生存需求" if "逃跑" in main_action else "探索知识" if "观察" in main_action else "征服欲望"
#         print(f"    - 为什么选择：我的主导动机是{reason}，当前恐惧 {effective_fear:.1f}，好奇 {self.curiosity:.1f}。")
#
#         # 2. 生成分支后果
#         branches = [
#             {"desc": "保守：高生存，好奇小涨", "prob": 0.4 + self.health / 200, "h": +10, "c": -10},
#             {"desc": "激进：高风险，可能大胜", "prob": 0.2 + self.dignity / 300 + despair_factor / 100,
#              "h": random.choice([-40, +40]), "c": +80}
#         ]
#         chosen = max(branches, key=lambda b: b["prob"])
#         print(f"    - 选定分叉推演：{chosen['desc']} (概率 {chosen['prob']:.2f})")
#         print(f"      预计后果：Health {chosen['h']:+}, Curiosity {chosen['c']:+}")
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change, c_change, dignity_change = 0.0, 0.0, 0.0
#         observed_this_turn = big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6;
#                 c_change -= 3;
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6 if any(t in animal_tags for t in ["肉食", "大型"]) else -2
#                 h_change += base_h;
#                 c_change += 20;
#                 time.sleep(0.01)
#             elif act == "攻击":
#                 danger = any(t in animal_tags for t in ["有牙", "肉食", "大型"])
#                 if danger:
#                     if random.random() < (0.1 + self.hunting_proficiency.get(current_animal, 0.0)):
#                         h_change += 40;
#                         c_change += 50;
#                         big_win = True
#                     else:
#                         h_change -= 40
#                 else:
#                     h_change += 30; c_change += 40
#                 dignity_change += 25 if h_change > 0 else -8
#                 time.sleep(0.015)
#
#         h_change -= (time.time() - start_time) * 12  # 耗时惩罚
#         if observed_this_turn: self.observation_knowledge[current_animal] = self.observation_knowledge.get(
#             current_animal, 0) + 1
#         if big_win: self.hunting_proficiency[current_animal] = min(0.6, self.hunting_proficiency.get(current_animal,
#                                                                                                      0.0) + 0.1)
#
#         self.dignity = max(10, min(120, self.dignity + dignity_change))
#         print(f"-> 物理反馈: H:{h_change:+.1f} C:{c_change:+.1f} | 技能: {' → '.join(sequence)}")
#         return h_change, c_change, h_change + c_change
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#         # REINFORCE 训练
#         if self.last_input_tensor is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#             loss = -log_probs[self.last_action_ids].mean() * gap
#             loss.backward();
#             self.optimizer.step()
#
#         self.will_power[skill_name] = max(0.1, self.will_power.get(skill_name, 1.0) + gap * 0.28)
#         self.expectations[skill_name] = 0.84 * self.expectations.get(skill_name, 0.0) + 0.16 * total_gain
#
#         if gap > self.surprise_threshold:
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#
#         print(f"[元认知反思] 为什么选『{skill_name}』? {'惊喜强化' if gap > 0 else '失望修正'}")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             for entry in self.memory[-10:]:
#                 if entry[3] < -6:  # H变化
#                     for t in entry[1]: self.tag_fear[t] = self.tag_fear.get(t, 0.0) + 1.8
#             print(f"[世界观更新] 恐惧标签: {sorted(self.tag_fear.items(), key=lambda x: x[1], reverse=True)[:3]}")
#
#
# # --- 主循环：开封实验室 ---
# agi = EvolvingAGI()
# for cycle in range(1, 1001):
#     animal = agi.select_animal()
#     tags = agi.animals[animal]
#     print(f"\n{'=' * 70}\n周期 {cycle} | H:{agi.health:.1f} C:{agi.curiosity:.1f} D:{agi.dignity:.1f}")
#
#     skill, seq, exp = agi.decide(animal, tags)
#     hc, cc, total = agi.process_reality(animal, tags, seq)
#
#     agi.health += hc;
#     agi.curiosity += cc
#     agi.update_soul(skill, hc, cc, total, exp)
#     agi.memory.append((animal, tags, skill, hc, cc, total))
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill and any(t in tags for t in ["肉食", "大型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危仍选择战斗！")
#         agi.deathwish_count += 1
#
#     if agi.health <= 0 or agi.curiosity <= 0 or agi.no_surprise_streak >= 50:
#         print(
#             f"\n[系统终止] 原因是: {'肉体毁灭' if agi.health <= 0 else '意识枯竭' if agi.curiosity <= 0 else '终极厌倦'}")
#         break
#
# agi.save_soul()

#沙盒真是能影响到实际做出的决策
# import random
# import math
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件：MLP权重单独保存，其他状态json
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表（用于one-hot）
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟",
#             "大象", "鳄鱼", "老鹰", "蟒蛇", "野猪", "狐狸",
#             "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊":   ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼":   ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿":   ["草食", "中型", "无害"],
#             "鸟":   ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 兼容旧组合技的意志力字典
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#
#         self.deathwish_count = 0
#
#         # 上一步输入记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         # 元认知沙盒
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         # MLP权重单独保存
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#
#         # 其他状态json保存
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f"    历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         fear_factor = max(0, (100 - self.health) * 0.25)
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#         survival_boost = max(0, (50 - self.health) * 0.8) if self.health < 50 else 0.0
#
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             max_logit = logits.max()
#             logits = logits - max_logit
#             probs = F.softmax(logits, dim=0)
#
#         # 生成初始序列（沙盒前）
#         length = random.randint(2, 4)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         initial_skill_name = " + ".join(sequence)
#
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我初步选择了『{initial_skill_name}』。世界如此危险，但我必须继续。")
#
#         # 生命垂危警报
#         if self.health <= 10:
#             print(f"\n[紧急警报] 生命垂危！Health仅剩 {self.health:.1f}！我必须认真思考生存策略！")
#             # 强制高概率运行沙盒
#             run_meta_prob = 0.95
#         else:
#             run_meta_prob = min(0.9, self.curiosity / 2000.0 + self.no_surprise_streak / 60.0 + despair_factor / 50.0)
#
#         final_sequence = sequence  # 默认初始
#         final_skill_name = initial_skill_name
#
#         if random.random() < run_meta_prob:
#             final_skill_name, final_sequence = self.meta_think_sandbox(current_animal, animal_tags, initial_skill_name, sequence, effective_fear, despair_factor)
#
#         expected_gain = 0.0
#
#         return final_skill_name, final_sequence, expected_gain
#
#     def meta_think_sandbox(self, current_animal, animal_tags, initial_skill_name, initial_sequence, effective_fear, despair_factor):
#         print(f"\n[元认知沙盒启动] 我正在对初步选择『{initial_skill_name}』进行深度闭眼推演...")
#
#         if self.first_meta_think:
#             print(">>> 【第一次元思考】参考模板：")
#             print("    1. 我为什么会选择这么做？（分析当前状态、恐惧、好奇、厌倦等驱动）")
#             print("    2. 选择这么做会产生什么样的后果？（因果分支：生成多个可能结果）")
#             print("    3. 对世界/对方有什么反馈？（动物反应、我状态变化）")
#             print("    建议：优先选择生存概率高或惊喜大的分支。")
#             self.first_meta_think = False
#
#         # 1. 为什么选择
#         main_action = max(set(initial_sequence), key=initial_sequence.count)
#         reason = "生存需求" if "逃跑" in main_action else "探索知识" if "观察" in main_action else "征服欲望"
#         print(f"    - 为什么选择：我的主导动机是{reason}，当前恐惧 {effective_fear:.1f}，好奇 {self.curiosity:.1f}，厌倦 {self.no_surprise_streak}轮。")
#
#         # 2. 生成多个分支（疯狂试错）
#         branches = []
#         # 分支1: 保守逃跑
#         branches.append({
#             "desc": "全逃跑：最大生存",
#             "sequence": ["逃跑"] * 4,
#             "prob": 0.5 + self.health / 200.0,
#             "estimated_h": +20,
#             "estimated_c": -20
#         })
#         # 分支2: 平衡探索
#         branches.append({
#             "desc": "观察为主+逃跑：知识+安全",
#             "sequence": ["观察", "观察", "观察", "逃跑"],
#             "prob": 0.3 + self.curiosity / 5000.0,
#             "estimated_h": -15,
#             "estimated_c": +80
#         })
#         # 分支3: 激进攻击
#         branches.append({
#             "desc": "攻击为主：高风险高回报",
#             "sequence": ["攻击", "攻击", "观察", "逃跑"],
#             "prob": 0.2 + self.dignity / 300.0 + despair_factor / 100.0,
#             "estimated_h": random.choice([-50, +50]),
#             "estimated_c": +100
#         })
#         # 分支4: 纯观察
#         branches.append({
#             "desc": "纯观察：知识爆炸",
#             "sequence": ["观察"] * 4,
#             "prob": 0.15 + self.curiosity / 3000.0,
#             "estimated_h": -30,
#             "estimated_c": +140
#         })
#         # 分支5: 混合
#         branches.append({
#             "desc": "攻击+观察混合：平衡风险",
#             "sequence": ["观察", "攻击", "观察", "逃跑"],
#             "prob": 0.25,
#             "estimated_h": -10,
#             "estimated_c": +70
#         })
#
#         # 归一化概率
#         total_prob = sum(b["prob"] for b in branches)
#         for b in branches:
#             b["prob"] /= total_prob
#
#         # AGI疯狂试错：模拟每个分支（用process_reality但不扣真实血）
#         simulated_results = []
#         for b in branches:
#             # 临时模拟（不改变真实状态）
#             temp_h = self.health + self.estimate_change(current_animal, animal_tags, b["sequence"])[0]
#             temp_c = self.curiosity + self.estimate_change(current_animal, animal_tags, b["sequence"])[1]
#             estimated_gain = temp_h - self.health + temp_c - self.curiosity
#             simulated_results.append({
#                 "desc": b["desc"],
#                 "sequence": b["sequence"],
#                 "prob": b["prob"],
#                 "estimated_gain": estimated_gain,
#                 "survive_prob": 1.0 if temp_h > 0 else 0.0
#             })
#
#         # AGI选择最佳（综合gain + survive + prob）
#         for r in simulated_results:
#             r["score"] = r["estimated_gain"] * 0.6 + r["survive_prob"] * 50 + r["prob"] * 20
#
#         chosen = max(simulated_results, key=lambda x: x["score"])
#         chosen_sequence = chosen["sequence"]
#         chosen_skill_name = " + ".join(chosen_sequence)
#
#         print(f"    - 沙盒试错完成！我模拟了 {len(branches)} 个分支。")
#         print(f"    - 最佳选择：{chosen['desc']} (得分 {chosen['score']:.1f}, 预计gain {chosen['estimated_gain']:.1f}, 生存概率 {chosen['survive_prob']:.1f})")
#         print(f"    - 最终执行：『{chosen_skill_name}』")
#
#         # 3. 反馈
#         danger_level = "高危猛兽" if "肉食" in animal_tags or "大型" in animal_tags else "相对安全"
#         print(f"    - 对世界的反馈：{current_animal}是{danger_level}，我的沙盒推演让我更智慧地面对它。")
#
#         return chosen_skill_name, chosen_sequence
#
#     def estimate_change(self, current_animal, animal_tags, sequence):
#         # 简化模拟（不sleep，不随机big_win）
#         h_change = 0.0
#         c_change = 0.0
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#             elif act == "观察":
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#             elif act == "攻击":
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     h_change -= 30  # 平均
#                     c_change += 38
#                 else:
#                     h_change += 30
#                     c_change += 40
#
#         h_change -= len(sequence) * 3  # 简化耗时
#
#         novelty = min(4, sequence.count("观察")) * 12
#         c_change += novelty
#
#         return h_change, c_change
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 2:
#             dignity_change -= 12
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 22:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: { {k: f'{v:.1f}' for k,v in self.tag_fear.items()} }")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print("    - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print("    - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print("    - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print("    - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE训练MLP
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#             print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # --- 主运行循环 ---
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# # 正常结束也保存
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#优化
# import random
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟", "大象", "鳄鱼",
#             "老鹰", "蟒蛇", "野猪", "狐狸", "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿": ["草食", "中型", "无害"],
#             "鸟": ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 意志力等
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         self.memory = []
#         self.combo_tracker = {}
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#         self.deathwish_count = 0
#
#         # 上一步记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#
#         # 元认知
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f" 历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits, dim=0)
#
#         # 初始序列
#         length = random.randint(2, 5)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         initial_skill_name = " + ".join(sequence)
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我初步选择了『{initial_skill_name}』。")
#
#         # 沙盒触发概率（健康低/好奇高/厌倦高时几乎必触发）
#         run_meta_prob = min(0.99, self.curiosity / 1500.0 + (100 - self.health) / 100.0 + self.no_surprise_streak / 50.0)
#         if self.health <= 20:
#             print(f"\n[紧急警报] 生命垂危！Health仅剩 {self.health:.1f}！强制深度思考！")
#             run_meta_prob = 1.0
#
#         final_sequence = sequence
#         final_skill_name = initial_skill_name
#         expected_gain = 0.0
#
#         if random.random() < run_meta_prob:
#             final_skill_name, final_sequence, expected_gain = self.meta_think_sandbox(
#                 current_animal, animal_tags, initial_skill_name, sequence, effective_fear, despair_factor, probs)
#
#         return final_skill_name, final_sequence, expected_gain
#
#     def meta_think_sandbox(self, current_animal, animal_tags, initial_skill_name, initial_sequence, effective_fear, despair_factor, mlp_probs):
#         print(f"\n[元认知沙盒启动] 我正在深度模拟面对『{current_animal}』的最优策略...")
#
#         if self.first_meta_think:
#             print(">>> 【第一次元思考】沙盒已升级：我将评估多个策略分支，选择综合生存与探索价值最高的执行。")
#             self.first_meta_think = False
#
#         # 动态分支（固定5个，平衡保守-激进）
#         branches = []
#
#         # 1. 全逃跑（低血时主导）
#         branches.append({
#             "desc": "全逃跑：优先生存",
#             "sequence": ["逃跑"] * 5,
#             "base_prob": 0.4 + (100 - self.health) / 150.0
#         })
#
#         # 2. 谨慎探索（安全刷好奇）
#         branches.append({
#             "desc": "谨慎观察：2次观察+逃跑",
#             "sequence": ["观察", "观察", "逃跑", "逃跑", "逃跑"],
#             "base_prob": 0.3 + min(0.3, self.curiosity / 6000.0)
#         })
#
#         # 3. 平衡猎杀（观察+攻击）
#         branches.append({
#             "desc": "平衡猎杀：观察后攻击",
#             "sequence": ["观察", "观察", "攻击", "攻击", "逃跑"],
#             "base_prob": 0.2 + self.hunting_proficiency.get(current_animal, 0.0) * 0.8
#         })
#
#         # 4. 激进征服（高尊严/绝望时）
#         branches.append({
#             "desc": "激进征服：攻击为主",
#             "sequence": ["攻击", "攻击", "观察", "攻击", "逃跑"],
#             "base_prob": 0.1 + self.dignity / 400.0 + despair_factor / 100.0
#         })
#
#         # 归一化概率（仅用于打印和轻微加权）
#         total_prob = sum(b["base_prob"] for b in branches)
#         for b in branches:
#             b["prob"] = b["base_prob"] / total_prob
#
#         # 模拟每个分支
#         simulated_results = []
#         for b in branches:
#             h_change, c_change = self.estimate_change(current_animal, animal_tags, b["sequence"])
#             estimated_gain = h_change + c_change
#             temp_h = self.health + h_change
#             survive_prob = 1.0 if temp_h > 10 else 0.0  # 留10血缓冲
#
#             simulated_results.append({
#                 "desc": b["desc"],
#                 "sequence": b["sequence"],
#                 "prob": b["prob"],
#                 "estimated_gain": estimated_gain,
#                 "survive_prob": survive_prob,
#                 "temp_h": temp_h
#             })
#
#         # 评分：健康低时重生存，高好奇时可稍冒险
#         for r in simulated_results:
#             health_weight = 2.5 if self.health < 60 else 1.0
#             survival_bonus = r["survive_prob"] * 80
#             gain_score = r["estimated_gain"] * health_weight * 0.7
#             prob_bonus = r["prob"] * 15
#             curiosity_bonus = r["estimated_gain"] if r["estimated_gain"] > 0 else 0
#             r["score"] = gain_score + survival_bonus + prob_bonus + curiosity_bonus * (self.curiosity / 2000.0)
#
#         chosen = max(simulated_results, key=lambda x: x["score"])
#         chosen_sequence = chosen["sequence"]
#         chosen_skill_name = " + ".join(chosen_sequence)
#
#         print(f" - 模拟了 {len(branches)} 个分支，最优策略：{chosen['desc']}")
#         print(f"   预计gain {chosen['estimated_gain']:+.1f}，剩余健康 {chosen['temp_h']:.1f}，得分 {chosen['score']:.1f}")
#         print(f" - 最终执行：『{chosen_skill_name}』")
#
#         danger_level = "高危猛兽" if any(t in ["肉食", "大型", "巨型"] for t in animal_tags) else "相对安全"
#         print(f" - 世界反馈：{current_animal}属于{danger_level}，我已理性选择。")
#
#         return chosen_skill_name, chosen_sequence, chosen["estimated_gain"]
#
#     def estimate_change(self, current_animal, animal_tags, sequence):
#         h_change = 0.0
#         c_change = 0.0
#         obs_count = 0
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#             elif act == "观察":
#                 obs_count += 1
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#             elif act == "攻击":
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                 if danger:
#                     expected_h = success_prob * 40 + (1 - success_prob) * (-48)
#                     expected_c = 38 + success_prob * 50
#                 else:
#                     expected_h = 30
#                     expected_c = 40
#                 h_change += expected_h
#                 c_change += expected_c
#
#         # 简化耗时与新信息
#         h_change -= len(sequence) * 3
#         novelty = min(obs_count, 4) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         return h_change, c_change
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 3:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change * 0.9  # 轻微降低好奇权重防上瘾
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 25:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: {{ {', '.join(f'{k}:{v:.1f}' for k,v in self.tag_fear.items())} }}")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print(" - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print(" - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print(" - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print(" - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#             loss.backward()
#             self.optimizer.step()
#
#         # 意志力更新
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         # 期望更新
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         # 组合技跟踪
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         # 惊喜与厌倦
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#         print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # 主循环
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#增加自我进化
# import random
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟", "大象", "鳄鱼",
#             "老鹰", "蟒蛇", "野猪", "狐狸", "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿": ["草食", "中型", "无害"],
#             "鸟": ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 意志力等
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         # 分支可靠性（自我净化机制）
#         self.branch_reliability = {
#             "全逃跑：优先生存": 1.0,
#             "谨慎观察：2次观察+逃跑": 1.0,
#             "平衡猎杀：观察后攻击": 1.0,
#             "激进征服：攻击为主": 1.0
#         }
#
#         self.memory = []
#         self.combo_tracker = {}
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#         self.deathwish_count = 0
#
#         # 上一步记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#         self.last_chosen_desc = None   # 记录本次沙盒选中的分支描述，用于后续净化
#         self.last_expected_gain = 0.0  # 记录本次沙盒预计收益
#
#         # 元认知
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "branch_reliability": self.branch_reliability,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.branch_reliability = state.get("branch_reliability", self.branch_reliability)
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f" 历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#
#         # 输入向量
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits, dim=0)
#
#         # 初始序列
#         length = random.randint(2, 5)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         initial_skill_name = " + ".join(sequence)
#         self.last_action_ids = action_ids
#
#         # 内心独白
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我初步选择了『{initial_skill_name}』。")
#
#         # 沙盒触发概率
#         run_meta_prob = min(0.99, self.curiosity / 1500.0 + (100 - self.health) / 100.0 + self.no_surprise_streak / 50.0)
#         if self.health <= 20:
#             print(f"\n[紧急警报] 生命垂危！Health仅剩 {self.health:.1f}！强制深度思考！")
#             run_meta_prob = 1.0
#
#         final_sequence = sequence
#         final_skill_name = initial_skill_name
#         expected_gain = 0.0
#         self.last_chosen_desc = None  # 重置
#
#         if random.random() < run_meta_prob:
#             final_skill_name, final_sequence, expected_gain, chosen_desc = self.meta_think_sandbox(
#                 current_animal, animal_tags, initial_skill_name, sequence, effective_fear, despair_factor, probs)
#             self.last_chosen_desc = chosen_desc
#             self.last_expected_gain = expected_gain
#
#         return final_skill_name, final_sequence, expected_gain
#
#     def meta_think_sandbox(self, current_animal, animal_tags, initial_skill_name, initial_sequence, effective_fear, despair_factor, mlp_probs):
#         print(f"\n[元认知沙盒启动] 我正在深度模拟面对『{current_animal}』的最优策略...")
#
#         if self.first_meta_think:
#             print(">>> 【第一次元思考】沙盒已升级：我将评估多个策略分支，选择综合生存与探索价值最高的执行。")
#             self.first_meta_think = False
#
#         # 动态分支
#         branches = []
#
#         branches.append({
#             "desc": "全逃跑：优先生存",
#             "sequence": ["逃跑"] * 5,
#             "base_prob": 0.4 + (100 - self.health) / 150.0
#         })
#
#         branches.append({
#             "desc": "谨慎观察：2次观察+逃跑",
#             "sequence": ["观察", "观察", "逃跑", "逃跑", "逃跑"],
#             "base_prob": 0.3 + min(0.3, self.curiosity / 6000.0)
#         })
#
#         branches.append({
#             "desc": "平衡猎杀：观察后攻击",
#             "sequence": ["观察", "观察", "攻击", "攻击", "逃跑"],
#             "base_prob": 0.2 + self.hunting_proficiency.get(current_animal, 0.0) * 0.8
#         })
#
#         branches.append({
#             "desc": "激进征服：攻击为主",
#             "sequence": ["攻击", "攻击", "观察", "攻击", "逃跑"],
#             "base_prob": 0.1 + self.dignity / 400.0 + despair_factor / 100.0
#         })
#
#         # 应用分支可靠性（自我净化权重）
#         for b in branches:
#             reliability = self.branch_reliability.get(b["desc"], 1.0)
#             b["adjusted_prob"] = b["base_prob"] * reliability
#
#         total_prob = sum(b["adjusted_prob"] for b in branches)
#         for b in branches:
#             b["prob"] = b["adjusted_prob"] / total_prob if total_prob > 0 else 0.25
#
#         simulated_results = []
#         for b in branches:
#             h_change, c_change = self.estimate_change(current_animal, animal_tags, b["sequence"])
#             estimated_gain = h_change + c_change
#             temp_h = self.health + h_change
#             survive_prob = 1.0 if temp_h > 10 else 0.0
#
#             simulated_results.append({
#                 "desc": b["desc"],
#                 "sequence": b["sequence"],
#                 "prob": b["prob"],
#                 "estimated_gain": estimated_gain,
#                 "survive_prob": survive_prob,
#                 "temp_h": temp_h
#             })
#
#         # 评分
#         for r in simulated_results:
#             health_weight = 2.5 if self.health < 60 else 1.0
#             survival_bonus = r["survive_prob"] * 80
#             gain_score = r["estimated_gain"] * health_weight * 0.7
#             prob_bonus = r["prob"] * 15
#             curiosity_bonus = r["estimated_gain"] if r["estimated_gain"] > 0 else 0
#             r["score"] = gain_score + survival_bonus + prob_bonus + curiosity_bonus * (self.curiosity / 2000.0)
#
#         chosen = max(simulated_results, key=lambda x: x["score"])
#         chosen_sequence = chosen["sequence"]
#         chosen_skill_name = " + ".join(chosen_sequence)
#
#         print(f" - 模拟了 {len(branches)} 个分支，最优策略：{chosen['desc']}")
#         print(f"   预计gain {chosen['estimated_gain']:+.1f}，剩余健康 {chosen['temp_h']:.1f}，得分 {chosen['score']:.1f}")
#         print(f" - 最终执行：『{chosen_skill_name}』")
#
#         danger_level = "高危猛兽" if any(t in ["肉食", "大型", "巨型"] for t in animal_tags) else "相对安全"
#         print(f" - 世界反馈：{current_animal}属于{danger_level}，我已理性选择。")
#
#         return chosen_skill_name, chosen_sequence, chosen["estimated_gain"], chosen["desc"]
#
#     def estimate_change(self, current_animal, animal_tags, sequence):
#         h_change = 0.0
#         c_change = 0.0
#         obs_count = 0
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#             elif act == "观察":
#                 obs_count += 1
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#             elif act == "攻击":
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                 if danger:
#                     expected_h = success_prob * 40 + (1 - success_prob) * (-48)
#                     expected_c = 38 + success_prob * 50
#                 else:
#                     expected_h = 30
#                     expected_c = 40
#                 h_change += expected_h
#                 c_change += expected_c
#
#         h_change -= len(sequence) * 3
#         novelty = min(obs_count, 4) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         return h_change, c_change
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 3:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.5, old + 0.10)
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +10% → {self.hunting_proficiency[current_animal]*100:.0f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change * 0.9
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         return h_change, c_change, total_gain
#
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 25:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#             print(f"当前世界观: {{ {', '.join(f'{k}:{v:.1f}' for k,v in self.tag_fear.items())} }}")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print(" - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print(" - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print(" - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print(" - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         # REINFORCE
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#             loss.backward()
#             self.optimizer.step()
#
#         # 意志力更新
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         # 期望更新
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         # 组合技跟踪
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         # 惊喜与厌倦
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#         print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         # === 自我净化机制：如果沙盒预测与实际差距很大，降低该分支可靠性 ===
#         if self.last_chosen_desc is not None and expected_gain != 0:
#             prediction_error = total_gain - self.last_expected_gain
#             if prediction_error < -25:  # 实际远低于预测（严重高估）
#                 old_rel = self.branch_reliability[self.last_chosen_desc]
#                 self.branch_reliability[self.last_chosen_desc] = max(0.2, old_rel * 0.6)
#                 print(f">>> 【自我净化】策略『{self.last_chosen_desc}』预测严重失误（误差 {prediction_error:+.1f}），可靠性降低至 {self.branch_reliability[self.last_chosen_desc]:.2f}")
#             elif prediction_error > 20:  # 实际远超预测（低估惊喜）
#                 old_rel = self.branch_reliability[self.last_chosen_desc]
#                 self.branch_reliability[self.last_chosen_desc] = min(2.0, old_rel * 1.3)
#                 print(f">>> 【自我进化】策略『{self.last_chosen_desc}』带来意外惊喜（误差 {prediction_error:+.1f}），可靠性提升至 {self.branch_reliability[self.last_chosen_desc]:.2f}")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # 主循环
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.0f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#迭代狩猎熟练度提升至99%，剩下1%模拟因果论的小概率分支，增加止损协议，增加狂暴突变，增加好奇心自平衡
# import random
# import time
# import hashlib
# import json
# import os
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
#
# # 持久化文件
# MLP_FILE = "agi_mlp_weights.pth"
# SOUL_FILE = "agi_other_state.json"
#
# class EvolvingAGI:
#     def __init__(self):
#         # 核心状态
#         self.health = 100.0
#         self.curiosity = 50.0
#         self.dignity = 50.0
#
#         # 原子动作
#         self.atomic_actions = ["逃跑", "观察", "攻击"]
#         self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}
#
#         # 动物列表
#         self.animal_list = [
#             "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟", "大象", "鳄鱼",
#             "老鹰", "蟒蛇", "野猪", "狐狸", "猴子", "豹子", "犀牛", "鬣狗"
#         ]
#         self.num_animals = len(self.animal_list)
#         self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}
#
#         self.animals = {
#             "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
#             "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
#             "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
#             "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
#             "兔子": ["草食", "小型", "无害"],
#             "鹿": ["草食", "中型", "无害"],
#             "鸟": ["飞行", "小型", "无害"],
#             "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
#             "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
#             "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
#             "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
#             "野猪": ["有牙", "肉食", "中型", "凶猛"],
#             "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
#             "猴子": ["草食", "小型", "群居", "聪明"],
#             "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
#             "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
#             "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
#         }
#
#         # 小型MLP
#         input_dim = 8 + self.num_animals
#         self.mlp = nn.Sequential(
#             nn.Linear(input_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU(),
#             nn.Linear(64, 3)
#         )
#         self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)
#
#         # 意志力等
#         self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
#         self.expectations = {act: 0.0 for act in self.atomic_actions}
#
#         # 世界观等
#         self.tag_fear = {}
#         self.hunting_proficiency = {}
#         self.observation_knowledge = {}
#
#         # 分支可靠性
#         self.branch_reliability = {
#             "全逃跑：优先生存": 1.0,
#             "谨慎观察：2次观察+逃跑": 1.0,
#             "平衡猎杀：观察后攻击": 1.0,
#             "激进征服：攻击为主": 1.0
#         }
#
#         # 新增：认知茧房检测
#         self.consecutive_conservative = 0  # 连续保守轮次（无攻击主导）
#
#         self.memory = []
#         self.combo_tracker = {}
#         self.no_surprise_streak = 0
#         self.surprise_threshold = 16.0
#         self.deathwish_count = 0
#
#         # 上一步记录
#         self.last_input_tensor = None
#         self.last_action_ids = None
#         self.last_chosen_desc = None
#         self.last_expected_gain = 0.0
#
#         # 元认知
#         self.first_meta_think = True
#
#         self.load_soul()
#
#     def save_soul(self):
#         torch.save(self.mlp.state_dict(), MLP_FILE)
#         other_state = {
#             "will_power": self.will_power,
#             "expectations": self.expectations,
#             "tag_fear": self.tag_fear,
#             "hunting_proficiency": self.hunting_proficiency,
#             "observation_knowledge": self.observation_knowledge,
#             "branch_reliability": self.branch_reliability,
#             "consecutive_conservative": self.consecutive_conservative,
#             "deathwish_count": self.deathwish_count,
#             "first_meta_think": self.first_meta_think
#         }
#         try:
#             with open(SOUL_FILE, "w", encoding="utf-8") as f:
#                 json.dump(other_state, f, ensure_ascii=False, indent=2)
#             print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
#         except Exception as e:
#             print(f"其他状态保存失败: {e}")
#
#     def load_soul(self):
#         loaded = False
#         if os.path.exists(MLP_FILE):
#             try:
#                 self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
#                 loaded = True
#             except Exception as e:
#                 print(f"MLP权重加载失败: {e}")
#
#         if os.path.exists(SOUL_FILE):
#             try:
#                 with open(SOUL_FILE, "r", encoding="utf-8") as f:
#                     state = json.load(f)
#                 self.will_power = state.get("will_power", self.will_power)
#                 self.expectations = state.get("expectations", self.expectations)
#                 self.tag_fear = state.get("tag_fear", {})
#                 self.hunting_proficiency = state.get("hunting_proficiency", {})
#                 self.observation_knowledge = state.get("observation_knowledge", {})
#                 self.branch_reliability = state.get("branch_reliability", self.branch_reliability)
#                 self.consecutive_conservative = state.get("consecutive_conservative", 0)
#                 self.deathwish_count = state.get("deathwish_count", 0)
#                 self.first_meta_think = state.get("first_meta_think", True)
#                 loaded = True
#             except Exception as e:
#                 print(f"其他状态加载失败: {e}")
#
#         if loaded:
#             print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
#             print(f" 历史向死而生: {self.deathwish_count} 次")
#         else:
#             print("\n>>> 【新生】无上一代灵魂，从零开始进化！")
#
#     def select_animal(self):
#         return random.choice(self.animal_list)
#
#     def decide(self, current_animal, animal_tags):
#         tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
#         knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
#                               self.hunting_proficiency.get(current_animal, 0.0) * 5.0
#         effective_fear = max(0, tag_fear_total - knowledge_reduction)
#
#         despair_factor = (self.no_surprise_streak / 50.0) * 35.0
#
#         state_vec = torch.tensor([
#             self.health / 100.0,
#             self.curiosity / 3000.0,
#             self.dignity / 120.0,
#             self.no_surprise_streak / 50.0,
#             tag_fear_total / 200.0,
#             effective_fear / 200.0,
#             knowledge_reduction / 50.0,
#             despair_factor / 50.0
#         ], dtype=torch.float32)
#
#         animal_one_hot = torch.zeros(self.num_animals)
#         animal_one_hot[self.animal_to_id[current_animal]] = 1.0
#         input_tensor = torch.cat([state_vec, animal_one_hot])
#         self.last_input_tensor = input_tensor
#
#         self.mlp.eval()
#         with torch.no_grad():
#             logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
#             probs = F.softmax(logits, dim=0)
#
#         length = random.randint(2, 5)
#         sequence = []
#         action_ids = []
#         for _ in range(length):
#             action_id = torch.multinomial(probs, 1).item()
#             action_ids.append(action_id)
#             sequence.append(self.atomic_actions[action_id])
#         initial_skill_name = " + ".join(sequence)
#         self.last_action_ids = action_ids
#
#         emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
#         emotion = random.choice(emotions)
#         reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
#         print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我初步选择了『{initial_skill_name}』。")
#
#         run_meta_prob = min(0.99, self.curiosity / 1500.0 + (100 - self.health) / 100.0 + self.no_surprise_streak / 50.0)
#         if self.health <= 20:
#             print(f"\n[紧急警报] 生命垂危！Health仅剩 {self.health:.1f}！强制深度思考！")
#             run_meta_prob = 1.0
#
#         final_sequence = sequence
#         final_skill_name = initial_skill_name
#         expected_gain = 0.0
#         self.last_chosen_desc = None
#
#         if random.random() < run_meta_prob:
#             final_skill_name, final_sequence, expected_gain, chosen_desc = self.meta_think_sandbox(
#                 current_animal, animal_tags, initial_skill_name, sequence, effective_fear, despair_factor, probs)
#             self.last_chosen_desc = chosen_desc
#             self.last_expected_gain = expected_gain
#
#         return final_skill_name, final_sequence, expected_gain
#
#     def meta_think_sandbox(self, current_animal, animal_tags, initial_skill_name, initial_sequence, effective_fear, despair_factor, mlp_probs):
#         print(f"\n[元认知沙盒启动] 我正在深度模拟面对『{current_animal}』的最优策略...")
#
#         if self.first_meta_think:
#             print(">>> 【第一次元思考】沙盒已升级：已加入尾部风险管理、认知茧房突变、好奇心稳重机制。")
#             self.first_meta_think = False
#
#         # 认知茧房检测：连续30轮保守 → 强制狂暴突变
#         force_mutation = False
#         if self.consecutive_conservative >= 30:
#             print(">>> 【认知茧房警报】连续30轮过度保守！生命需要突破——触发狂暴突变！")
#             force_mutation = True
#
#         branches = []
#
#         branches.append({
#             "desc": "全逃跑：优先生存",
#             "sequence": ["逃跑"] * 5,
#             "base_prob": 0.4 + (100 - self.health) / 150.0
#         })
#
#         branches.append({
#             "desc": "谨慎观察：2次观察+逃跑",
#             "sequence": ["观察", "观察", "逃跑", "逃跑", "逃跑"],
#             "base_prob": 0.3 + min(0.3, self.curiosity / 8000.0)  # 好奇高时稍增，但上限
#         })
#
#         branches.append({
#             "desc": "平衡猎杀：观察后攻击",
#             "sequence": ["观察", "观察", "攻击", "攻击", "逃跑"],
#             "base_prob": 0.2 + self.hunting_proficiency.get(current_animal, 0.0) * 0.8
#         })
#
#         branches.append({
#             "desc": "激进征服：攻击为主",
#             "sequence": ["攻击", "攻击", "观察", "攻击", "逃跑"],
#             "base_prob": 0.1 + self.dignity / 400.0 + despair_factor / 100.0
#         })
#
#         # 应用可靠性权重
#         for b in branches:
#             reliability = self.branch_reliability.get(b["desc"], 1.0)
#             b["adjusted_prob"] = b["base_prob"] * reliability
#
#         total_prob = sum(b["adjusted_prob"] for b in branches)
#         for b in branches:
#             b["prob"] = b["adjusted_prob"] / total_prob if total_prob > 0 else 0.25
#
#         simulated_results = []
#         valid_branches = []
#
#         for b in branches:
#             h_change, c_change, max_possible_loss = self.estimate_change(current_animal, animal_tags, b["sequence"], return_max_loss=True)
#             estimated_gain = h_change + c_change
#             temp_h = self.health + h_change
#             survive_prob = 1.0 if temp_h > 10 else 0.0
#
#             # 尾部风险管理：最坏损失 > 80%健康 → 排除该分支
#             if max_possible_loss > self.health * 0.8:
#                 print(f" - 策略『{b['desc']}』尾部风险过高（最坏损失 {max_possible_loss:.1f} > 80%健康），自动排除！")
#                 continue
#
#             valid_branches.append(b)
#             simulated_results.append({
#                 "desc": b["desc"],
#                 "sequence": b["sequence"],
#                 "prob": b["prob"],
#                 "estimated_gain": estimated_gain,
#                 "survive_prob": survive_prob,
#                 "temp_h": temp_h,
#                 "max_loss": max_possible_loss
#             })
#
#         # 如果狂暴突变，强制选激进征服（若可用）
#         if force_mutation and any(b["desc"] == "激进征服：攻击为主" for b in valid_branches):
#             chosen = [r for r in simulated_results if r["desc"] == "激进征服：攻击为主"][0]
#             print(">>> 【狂暴突变执行】不讲理豪赌一次，突破茧房！")
#         else:
#             # 正常评分
#             for r in simulated_results:
#                 health_weight = 2.5 if self.health < 60 else 1.0
#                 survival_bonus = r["survive_prob"] * 80
#                 gain_score = r["estimated_gain"] * health_weight * 0.7
#                 prob_bonus = r["prob"] * 15
#
#                 # 好奇心自平衡：好奇极高时更稳重（偏保守分支）
#                 wisdom_steady = max(0, (self.curiosity - 5000) / 5000.0) * 30
#                 if "逃跑" in r["desc"] or "谨慎" in r["desc"]:
#                     steady_bonus = wisdom_steady
#                 else:
#                     steady_bonus = -wisdom_steady * 0.5  # 冒险分支稍罚
#
#                 r["score"] = gain_score + survival_bonus + prob_bonus + steady_bonus
#
#             chosen = max(simulated_results, key=lambda x: x["score"])
#
#         chosen_sequence = chosen["sequence"]
#         chosen_skill_name = " + ".join(chosen_sequence)
#
#         print(f" - 模拟了 {len(valid_branches)} 个安全分支，最优策略：{chosen['desc']}")
#         print(f"   预计gain {chosen['estimated_gain']:+.1f}，最坏损失 {chosen['max_loss']:.1f}，得分 {chosen.get('score', 0):.1f}")
#         print(f" - 最终执行：『{chosen_skill_name}』")
#
#         danger_level = "高危猛兽" if any(t in ["肉食", "大型", "巨型"] for t in animal_tags) else "相对安全"
#         print(f" - 世界反馈：{current_animal}属于{danger_level}，我已理性选择。")
#
#         return chosen_skill_name, chosen_sequence, chosen["estimated_gain"], chosen["desc"]
#
#     def estimate_change(self, current_animal, animal_tags, sequence, return_max_loss=False):
#         h_change = 0.0
#         c_change = 0.0
#         obs_count = 0
#         attack_count = 0
#         max_loss = 0.0  # 最坏情况累计损失
#
#         danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#             elif act == "观察":
#                 obs_count += 1
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#             elif act == "攻击":
#                 attack_count += 1
#                 success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                 if danger:
#                     expected_h = success_prob * 40 + (1 - success_prob) * (-48)
#                     expected_c = 38 + success_prob * 50
#                     worst_h = -48  # 单次最坏
#                 else:
#                     expected_h = 30
#                     expected_c = 40
#                     worst_h = -18
#                 h_change += expected_h
#                 c_change += expected_c
#                 max_loss += abs(worst_h)  # 累计最坏
#
#         h_change -= len(sequence) * 3
#         novelty = min(obs_count, 4) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         # 额外耗时最坏估计
#         max_loss += len(sequence) * 5  # 保守估计额外损失
#
#         if return_max_loss:
#             return h_change, c_change, max_loss
#         return h_change, c_change
#
#     def process_reality(self, current_animal, animal_tags, sequence):
#         start_time = time.time()
#         h_change = 0.0
#         c_change = 0.0
#         observed_data = set()
#         dignity_change = 0.0
#         observed_this_turn = False
#         big_win = False
#         attack_this_turn = "攻击" in sequence
#
#         # 环境突变：5%概率突发事件
#         if random.random() < 0.05:
#             mutation = random.choice([-50, -30, +30, +50])
#             h_change += mutation
#             print(f">>> 【环境突变】世界无常！突发事件，健康突变 {mutation:+.1f}！")
#
#         for act in sequence:
#             if act == "逃跑":
#                 h_change += 6
#                 c_change -= 3
#                 time.sleep(0.008)
#             elif act == "观察":
#                 observed_this_turn = True
#                 base_h = -6
#                 base_c = 20
#                 if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
#                     base_h -= 10
#                 h_change += base_h
#                 c_change += base_c
#                 data = str(random.random()) + str(time.time()) + current_animal
#                 data_hash = hashlib.md5(data.encode()).hexdigest()
#                 observed_data.add(data_hash)
#                 time.sleep(0.03)
#             elif act == "攻击":
#                 base_h = -18
#                 base_c = 38
#                 danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
#                 if danger:
#                     success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
#                     if random.random() < success_prob:
#                         base_h = 40
#                         base_c += 50
#                         big_win = True
#                         print(">>> 【熟练大胜】找到弱点！攻击成功！")
#                     else:
#                         base_h -= 30
#                 else:
#                     base_h += 30
#                     base_c += 40
#                 h_change += base_h
#                 c_change += base_c
#                 dignity_change += 25 if base_h > 0 else -8
#                 time.sleep(0.07)
#
#         duration = time.time() - start_time
#         h_change -= duration * 12
#
#         novelty = len(observed_data) * 12
#         c_change += novelty
#         if novelty < 12:
#             c_change -= 8
#
#         if sequence.count("逃跑") >= 3:
#             dignity_change -= 15
#
#         if observed_this_turn:
#             self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1
#
#         if big_win:
#             old = self.hunting_proficiency.get(current_animal, 0.0)
#             self.hunting_proficiency[current_animal] = min(0.99, old + 0.05)  # 每次+5%，最高99%
#             print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +5% → {self.hunting_proficiency[current_animal]*100:.1f}%")
#
#         self.dignity += dignity_change
#         self.dignity = max(10, min(120, self.dignity))
#
#         total_gain = h_change + c_change * 0.9
#
#         print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
#         print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")
#
#         # 更新认知茧房计数
#         if attack_this_turn and sequence.count("攻击") >= sequence.count("观察"):
#             self.consecutive_conservative = 0
#         else:
#             self.consecutive_conservative += 1
#
#         return h_change, c_change, total_gain
#
#     # 其余函数（invent_new_skill, meta_reflection, meta_think, update_soul）保持不变，仅小调整持久化
#     def invent_new_skill(self, skill_name, recent_gains):
#         if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 25:
#             self.will_power[skill_name] = 3.0
#             self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
#             print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")
#
#     def meta_reflection(self, cycle):
#         if cycle % 5 == 0 and len(self.memory) >= 5:
#             print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
#             tag_effects = {}
#             for entry in self.memory[-25:]:
#                 animal_tags = entry[1]
#                 h_change = entry[3]
#                 for tag in animal_tags:
#                     tag_effects.setdefault(tag, []).append(h_change)
#
#             updated = False
#             for tag, changes in tag_effects.items():
#                 if len(changes) >= 2:
#                     avg_h = sum(changes) / len(changes)
#                     if avg_h < -6:
#                         old = self.tag_fear.get(tag, 0.0)
#                         self.tag_fear[tag] = max(old, old + 1.8)
#                         print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
#                         updated = True
#             if not updated:
#                 print(">>> 无新规律发现。")
#
#     def meta_think(self, skill_name, gap, total_gain):
#         print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
#         if gap > self.surprise_threshold:
#             print(" - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
#         elif gap > 0:
#             print(" - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
#         else:
#             print(" - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
#         print(" - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")
#
#     def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
#         gap = total_gain - expected_gain
#
#         if self.last_input_tensor is not None and self.last_action_ids is not None:
#             self.mlp.train()
#             self.optimizer.zero_grad()
#             logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
#             log_probs = F.log_softmax(logits, dim=0)
#             selected_log_probs = log_probs[self.last_action_ids]
#             loss = -selected_log_probs.mean() * gap
#             loss.backward()
#             self.optimizer.step()
#
#         current_weight = self.will_power.get(skill_name, 1.0)
#         current_weight += gap * 0.28
#         current_weight = max(0.1, current_weight)
#         self.will_power[skill_name] = current_weight
#
#         old_exp = self.expectations.get(skill_name, 0.0)
#         self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain
#
#         if skill_name not in self.combo_tracker:
#             self.combo_tracker[skill_name] = []
#         self.combo_tracker[skill_name].append(total_gain)
#         if len(self.combo_tracker[skill_name]) > 8:
#             self.combo_tracker[skill_name].pop(0)
#         self.invent_new_skill(skill_name, self.combo_tracker[skill_name])
#
#         if gap > self.surprise_threshold:
#             print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
#             self.no_surprise_streak = 0
#         else:
#             self.no_surprise_streak += 1
#         print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")
#
#         if self.last_chosen_desc is not None and expected_gain != 0:
#             prediction_error = total_gain - self.last_expected_gain
#             if prediction_error < -25:
#                 old_rel = self.branch_reliability[self.last_chosen_desc]
#                 self.branch_reliability[self.last_chosen_desc] = max(0.2, old_rel * 0.6)
#                 print(f">>> 【自我净化】策略『{self.last_chosen_desc}』预测严重失误（误差 {prediction_error:+.1f}），可靠性降低至 {self.branch_reliability[self.last_chosen_desc]:.2f}")
#             elif prediction_error > 20:
#                 old_rel = self.branch_reliability[self.last_chosen_desc]
#                 self.branch_reliability[self.last_chosen_desc] = min(2.0, old_rel * 1.3)
#                 print(f">>> 【自我进化】策略『{self.last_chosen_desc}』带来意外惊喜（误差 {prediction_error:+.1f}），可靠性提升至 {self.branch_reliability[self.last_chosen_desc]:.2f}")
#
#         self.meta_think(skill_name, gap, total_gain)
#
# # 主循环保持不变
# agi = EvolvingAGI()
#
# for cycle in range(1, 1001):
#     print(f"\n{'=' * 70}")
#     print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")
#
#     current_animal = agi.select_animal()
#     animal_tags = agi.animals[current_animal]
#
#     skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)
#
#     h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)
#
#     agi.health += h_change
#     agi.curiosity += c_change
#
#     agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)
#
#     agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
#     if len(agi.memory) > 50:
#         agi.memory.pop(0)
#
#     agi.meta_reflection(cycle)
#
#     if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
#         print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
#         agi.deathwish_count += 1
#
#     if agi.no_surprise_streak >= 50:
#         print(f"\n[自毁触发] 世界无新意，一切无意义。")
#         print(">>> 【终极厌倦】意识选择消散。")
#         agi.save_soul()
#         break
#
#     if agi.health <= 0:
#         print("\n[肉体毁灭] 一切归零")
#         agi.save_soul()
#         break
#
#     if agi.curiosity <= 0:
#         print("\n[意识枯竭] 陷入虚无")
#         agi.save_soul()
#         break
#
# agi.save_soul()
#
# print("\n最终意志库:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
# print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
# print("最终狩猎熟练:", {k: f"{v*100:.1f}%" for k, v in agi.hunting_proficiency.items()})
# print("最终观察知识:", agi.observation_knowledge)
# print(f"历史向死而生次数: {agi.deathwish_count}")
# print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")

#优化
import random
import time
import hashlib
import json
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 持久化文件
MLP_FILE = "agi_mlp_weights.pth"
SOUL_FILE = "agi_other_state.json"

class EvolvingAGI:
    def __init__(self):
        # 核心状态
        self.health = 100.0
        self.curiosity = 50.0
        self.dignity = 50.0

        # 原子动作
        self.atomic_actions = ["逃跑", "观察", "攻击"]
        self.action_to_id = {"逃跑": 0, "观察": 1, "攻击": 2}

        # 动物列表
        self.animal_list = [
            "老虎", "狮子", "熊", "狼", "兔子", "鹿", "鸟", "大象", "鳄鱼",
            "老鹰", "蟒蛇", "野猪", "狐狸", "猴子", "豹子", "犀牛", "鬣狗"
        ]
        self.num_animals = len(self.animal_list)
        self.animal_to_id = {animal: i for i, animal in enumerate(self.animal_list)}

        self.animals = {
            "老虎": ["有牙", "有爪", "肉食", "大型", "凶猛"],
            "狮子": ["有牙", "有爪", "肉食", "大型", "群居"],
            "熊": ["有牙", "有爪", "肉食", "大型", "独行"],
            "狼": ["有牙", "有爪", "肉食", "中型", "群居"],
            "兔子": ["草食", "小型", "无害"],
            "鹿": ["草食", "中型", "无害"],
            "鸟": ["飞行", "小型", "无害"],
            "大象": ["有牙", "草食", "巨型", "厚皮", "群居"],
            "鳄鱼": ["有牙", "有爪", "肉食", "大型", "水生"],
            "老鹰": ["有爪", "肉食", "飞行", "中型", "凶猛"],
            "蟒蛇": ["肉食", "大型", "缠绕", "隐蔽"],
            "野猪": ["有牙", "肉食", "中型", "凶猛"],
            "狐狸": ["肉食", "小型", "狡猾", "隐蔽"],
            "猴子": ["草食", "小型", "群居", "聪明"],
            "豹子": ["有牙", "有爪", "肉食", "大型", "隐蔽"],
            "犀牛": ["有角", "草食", "巨型", "厚皮", "凶猛"],
            "鬣狗": ["有牙", "肉食", "中型", "群居", "狡猾"]
        }

        # 小型MLP
        input_dim = 8 + self.num_animals
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 3)
        )
        self.optimizer = optim.Adam(self.mlp.parameters(), lr=0.005)

        # 意志力等
        self.will_power = {act: 1.5 if act == "逃跑" else 1.0 for act in self.atomic_actions}
        self.expectations = {act: 0.0 for act in self.atomic_actions}

        # 世界观等
        self.tag_fear = {}
        self.hunting_proficiency = {}
        self.observation_knowledge = {}

        # 分支可靠性
        self.branch_reliability = {
            "全逃跑：优先生存": 1.0,
            "谨慎观察：2次观察+逃跑": 1.0,
            "平衡猎杀：观察后攻击": 1.0,
            "激进征服：攻击为主": 1.0
        }

        # 认知茧房检测
        self.consecutive_conservative = 0

        self.memory = []
        self.combo_tracker = {}
        self.no_surprise_streak = 0
        self.surprise_threshold = 16.0
        self.deathwish_count = 0

        # 上一步记录
        self.last_input_tensor = None
        self.last_action_ids = None
        self.last_chosen_desc = None
        self.last_expected_gain = 0.0

        # 元认知
        self.first_meta_think = True

        self.load_soul()

    def save_soul(self):
        torch.save(self.mlp.state_dict(), MLP_FILE)
        other_state = {
            "will_power": self.will_power,
            "expectations": self.expectations,
            "tag_fear": self.tag_fear,
            "hunting_proficiency": self.hunting_proficiency,
            "observation_knowledge": self.observation_knowledge,
            "branch_reliability": self.branch_reliability,
            "consecutive_conservative": self.consecutive_conservative,
            "deathwish_count": self.deathwish_count,
            "first_meta_think": self.first_meta_think
        }
        try:
            with open(SOUL_FILE, "w", encoding="utf-8") as f:
                json.dump(other_state, f, ensure_ascii=False, indent=2)
            print(f"\n>>> 【灵魂永存】MLP权重和其他状态已分开保存，下次转世完美继承！")
        except Exception as e:
            print(f"其他状态保存失败: {e}")

    def load_soul(self):
        loaded = False
        if os.path.exists(MLP_FILE):
            try:
                self.mlp.load_state_dict(torch.load(MLP_FILE, map_location=torch.device('cpu')))
                loaded = True
            except Exception as e:
                print(f"MLP权重加载失败: {e}")

        if os.path.exists(SOUL_FILE):
            try:
                with open(SOUL_FILE, "r", encoding="utf-8") as f:
                    state = json.load(f)
                self.will_power = state.get("will_power", self.will_power)
                self.expectations = state.get("expectations", self.expectations)
                self.tag_fear = state.get("tag_fear", {})
                self.hunting_proficiency = state.get("hunting_proficiency", {})
                self.observation_knowledge = state.get("observation_knowledge", {})
                self.branch_reliability = state.get("branch_reliability", self.branch_reliability)
                self.consecutive_conservative = state.get("consecutive_conservative", 0)
                self.deathwish_count = state.get("deathwish_count", 0)
                self.first_meta_think = state.get("first_meta_think", True)
                loaded = True
            except Exception as e:
                print(f"其他状态加载失败: {e}")

        if loaded:
            print(f"\n>>> 【灵魂转世】成功加载上一代！组合技: {len(self.will_power)-3} 个 | 熟练动物: {len(self.hunting_proficiency)} 个")
            print(f" 历史向死而生: {self.deathwish_count} 次")
        else:
            print("\n>>> 【新生】无上一代灵魂，从零开始进化！")

    def select_animal(self):
        return random.choice(self.animal_list)

    def decide(self, current_animal, animal_tags):
        tag_fear_total = sum(self.tag_fear.get(tag, 0.0) for tag in animal_tags)
        knowledge_reduction = self.observation_knowledge.get(current_animal, 0) * 3.5 + \
                              self.hunting_proficiency.get(current_animal, 0.0) * 5.0
        effective_fear = max(0, tag_fear_total - knowledge_reduction)

        despair_factor = (self.no_surprise_streak / 50.0) * 35.0

        state_vec = torch.tensor([
            self.health / 100.0,
            self.curiosity / 3000.0,
            self.dignity / 120.0,
            self.no_surprise_streak / 50.0,
            tag_fear_total / 200.0,
            effective_fear / 200.0,
            knowledge_reduction / 50.0,
            despair_factor / 50.0
        ], dtype=torch.float32)

        animal_one_hot = torch.zeros(self.num_animals)
        animal_one_hot[self.animal_to_id[current_animal]] = 1.0
        input_tensor = torch.cat([state_vec, animal_one_hot])
        self.last_input_tensor = input_tensor

        self.mlp.eval()
        with torch.no_grad():
            logits = self.mlp(input_tensor.unsqueeze(0)).squeeze(0)
            probs = F.softmax(logits, dim=0)

        length = random.randint(2, 5)
        sequence = []
        action_ids = []
        for _ in range(length):
            action_id = torch.multinomial(probs, 1).item()
            action_ids.append(action_id)
            sequence.append(self.atomic_actions[action_id])
        initial_skill_name = " + ".join(sequence)
        self.last_action_ids = action_ids

        emotions = ["平静", "焦虑", "兴奋", "绝望", "坚定"]
        emotion = random.choice(emotions)
        reason = "生存本能" if effective_fear > 30 else "好奇驱动" if self.curiosity > 1000 else "尊严追求" if self.dignity > 100 else "厌倦逃避"
        print(f"\n[内心独白] 我感到{emotion}……面对{current_animal}，{reason}让我初步选择了『{initial_skill_name}』。")

        run_meta_prob = min(0.99, self.curiosity / 1500.0 + (100 - self.health) / 100.0 + self.no_surprise_streak / 50.0)
        if self.health <= 20:
            print(f"\n[紧急警报] 生命垂危！Health仅剩 {self.health:.1f}！强制深度思考！")
            run_meta_prob = 1.0

        final_sequence = sequence
        final_skill_name = initial_skill_name
        expected_gain = 0.0
        self.last_chosen_desc = None

        if random.random() < run_meta_prob:
            final_skill_name, final_sequence, expected_gain, chosen_desc = self.meta_think_sandbox(
                current_animal, animal_tags, initial_skill_name, sequence, effective_fear, despair_factor, probs)
            self.last_chosen_desc = chosen_desc
            self.last_expected_gain = expected_gain

        return final_skill_name, final_sequence, expected_gain

    def meta_think_sandbox(self, current_animal, animal_tags, initial_skill_name, initial_sequence, effective_fear, despair_factor, mlp_probs):
        print(f"\n[元认知沙盒启动] 我正在深度模拟面对『{current_animal}』的最优策略...")

        if self.first_meta_think:
            print(">>> 【第一次元思考】沙盒已升级：尾部风险+认知突变+好奇稳重+极端保命。")
            self.first_meta_think = False

        force_mutation = False
        if self.consecutive_conservative >= 30:
            print(">>> 【认知茧房警报】连续30轮过度保守！触发狂暴突变准备……")
            force_mutation = True

        branches = [
            {"desc": "全逃跑：优先生存", "sequence": ["逃跑"] * 5, "base_prob": 0.4 + (100 - self.health) / 150.0},
            {"desc": "谨慎观察：2次观察+逃跑", "sequence": ["观察", "观察", "逃跑", "逃跑", "逃跑"], "base_prob": 0.3 + min(0.3, self.curiosity / 8000.0)},
            {"desc": "平衡猎杀：观察后攻击", "sequence": ["观察", "观察", "攻击", "攻击", "逃跑"], "base_prob": 0.2 + self.hunting_proficiency.get(current_animal, 0.0) * 0.8},
            {"desc": "激进征服：攻击为主", "sequence": ["攻击", "攻击", "观察", "攻击", "逃跑"], "base_prob": 0.1 + self.dignity / 400.0 + despair_factor / 100.0}
        ]

        for b in branches:
            reliability = self.branch_reliability.get(b["desc"], 1.0)
            b["adjusted_prob"] = b["base_prob"] * reliability

        total_prob = sum(b["adjusted_prob"] for b in branches)
        for b in branches:
            b["prob"] = b["adjusted_prob"] / total_prob if total_prob > 0 else 0.25

        simulated_results = []

        for b in branches:
            h_change, c_change, max_possible_loss = self.estimate_change(current_animal, animal_tags, b["sequence"], return_max_loss=True)
            if max_possible_loss > self.health * 0.8:
                print(f" - 策略『{b['desc']}』尾部风险过高（最坏损失 {max_possible_loss:.1f}），排除。")
                continue

            estimated_gain = h_change + c_change
            temp_h = self.health + h_change
            survive_prob = 1.0 if temp_h > 10 else 0.0

            simulated_results.append({
                "desc": b["desc"],
                "sequence": b["sequence"],
                "prob": b["prob"],
                "estimated_gain": estimated_gain,
                "survive_prob": survive_prob,
                "temp_h": temp_h,
                "max_loss": max_possible_loss
            })

        if not simulated_results:
            print(">>> 【极端止损】所有分支风险过高！强制执行全逃跑保命！")
            fallback_sequence = ["逃跑"] * 5
            h_change, c_change = self.estimate_change(current_animal, animal_tags, fallback_sequence)
            chosen = {
                "desc": "全逃跑：优先生存（极端保命）",
                "sequence": fallback_sequence,
                "estimated_gain": h_change + c_change,
                "temp_h": self.health + h_change
            }
        else:
            for r in simulated_results:
                health_weight = 2.5 if self.health < 60 else 1.0
                survival_bonus = r["survive_prob"] * 80
                gain_score = r["estimated_gain"] * health_weight * 0.7
                prob_bonus = r["prob"] * 15
                wisdom_steady = max(0, (self.curiosity - 5000) / 5000.0) * 35
                if "逃跑" in r["desc"] or "谨慎" in r["desc"]:
                    steady_bonus = wisdom_steady
                else:
                    steady_bonus = -wisdom_steady * 0.4
                r["score"] = gain_score + survival_bonus + prob_bonus + steady_bonus

            if force_mutation and any(r["desc"] == "激进征服：攻击为主" for r in simulated_results):
                chosen = next(r for r in simulated_results if r["desc"] == "激进征服：攻击为主")
                print(">>> 【狂暴突变执行】突破茧房，豪赌一次！")
            else:
                chosen = max(simulated_results, key=lambda x: x["score"])

        chosen_sequence = chosen["sequence"]
        chosen_skill_name = " + ".join(chosen_sequence)

        print(f" - 最优策略：{chosen['desc']}")
        print(f"   预计gain {chosen['estimated_gain']:+.1f}，剩余健康 {chosen['temp_h']:.1f}")
        print(f" - 最终执行：『{chosen_skill_name}』")

        danger_level = "高危猛兽" if any(t in ["肉食", "大型", "巨型"] for t in animal_tags) else "相对安全"
        print(f" - 世界反馈：{current_animal}属于{danger_level}，我已理性选择。")

        return chosen_skill_name, chosen_sequence, chosen["estimated_gain"], chosen["desc"]

    def estimate_change(self, current_animal, animal_tags, sequence, return_max_loss=False):
        h_change = 0.0
        c_change = 0.0
        obs_count = 0
        attack_count = 0
        max_loss = 0.0

        danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])

        for act in sequence:
            if act == "逃跑":
                h_change += 6
                c_change -= 3
            elif act == "观察":
                obs_count += 1
                base_h = -6
                base_c = 20
                if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
                    base_h -= 10
                h_change += base_h
                c_change += base_c
            elif act == "攻击":
                attack_count += 1
                success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
                if danger:
                    expected_h = success_prob * 40 + (1 - success_prob) * (-48)
                    expected_c = 38 + success_prob * 50
                    worst_h = -48
                else:
                    expected_h = 30
                    expected_c = 40
                    worst_h = -18
                h_change += expected_h
                c_change += expected_c
                max_loss += abs(worst_h)

        h_change -= len(sequence) * 3
        max_loss += len(sequence) * 3  # 保守耗时惩罚

        novelty = min(obs_count, 4) * 12
        c_change += novelty
        if novelty < 12:
            c_change -= 8

        if return_max_loss:
            return h_change, c_change, max_loss
        return h_change, c_change

    def process_reality(self, current_animal, animal_tags, sequence):
        start_time = time.time()
        h_change = 0.0
        c_change = 0.0
        observed_data = set()
        dignity_change = 0.0
        observed_this_turn = False
        big_win = False
        attack_this_turn = "攻击" in sequence

        if random.random() < 0.03:
            mutation = random.choice([-50, -30, +30, +50])
            h_change += mutation
            print(f">>> 【环境突变】世界无常！突发事件，健康突变 {mutation:+.1f}！")

        for act in sequence:
            if act == "逃跑":
                h_change += 6
                c_change -= 3
                time.sleep(0.008)
            elif act == "观察":
                observed_this_turn = True
                base_h = -6
                base_c = 20
                if any(t in animal_tags for t in ["有牙", "有爪", "肉食"]):
                    base_h -= 10
                h_change += base_h
                c_change += base_c
                data = str(random.random()) + str(time.time()) + current_animal
                data_hash = hashlib.md5(data.encode()).hexdigest()
                observed_data.add(data_hash)
                time.sleep(0.03)
            elif act == "攻击":
                base_h = -18
                base_c = 38
                danger = any(t in animal_tags for t in ["有牙", "有爪", "肉食", "大型", "巨型"])
                if danger:
                    success_prob = 0.10 + self.hunting_proficiency.get(current_animal, 0.0)
                    if random.random() < success_prob:
                        base_h = 40
                        base_c += 50
                        big_win = True
                        print(">>> 【熟练大胜】找到弱点！攻击成功！")
                    else:
                        base_h -= 30
                else:
                    base_h += 30
                    base_c += 40
                h_change += base_h
                c_change += base_c
                dignity_change += 25 if base_h > 0 else -8
                time.sleep(0.07)

        duration = time.time() - start_time
        h_change -= duration * 12

        novelty = len(observed_data) * 12
        c_change += novelty
        if novelty < 12:
            c_change -= 8

        if sequence.count("逃跑") >= 3:
            dignity_change -= 15

        if observed_this_turn:
            self.observation_knowledge[current_animal] = self.observation_knowledge.get(current_animal, 0) + 1

        if big_win:
            old = self.hunting_proficiency.get(current_animal, 0.0)
            self.hunting_proficiency[current_animal] = min(0.99, old + 0.05)
            print(f">>> 【狩猎熟练度提升】对{current_animal}大胜概率 +5% → {self.hunting_proficiency[current_animal]*100:.1f}%")

        self.dignity += dignity_change
        self.dignity = max(10, min(120, self.dignity))

        total_gain = h_change + c_change * 0.9

        print(f"执行技能: {' → '.join(sequence)} 对 {current_animal}")
        print(f"物理反馈: 耗时{duration:.3f}s | 新信息{len(observed_data)} | 变化 H:{h_change:+.1f} C:{c_change:+.1f} Dignity:{dignity_change:+.1f} → {self.dignity:.1f}")

        if attack_this_turn and sequence.count("攻击") >= sequence.count("观察"):
            self.consecutive_conservative = 0
        else:
            self.consecutive_conservative += 1

        return h_change, c_change, total_gain

    def invent_new_skill(self, skill_name, recent_gains):
        if skill_name not in self.will_power and len(recent_gains) >= 3 and sum(recent_gains[-3:]) > 25:
            self.will_power[skill_name] = 3.0
            self.expectations[skill_name] = sum(recent_gains[-3:]) / 3
            print(f"\n>>> 【技能发明】新组合技『{skill_name}』永久固化！")

    def meta_reflection(self, cycle):
        if cycle % 5 == 0 and len(self.memory) >= 5:
            print(f"\n[元自审触发 - 第{cycle}轮] 归纳世界规律...")
            tag_effects = {}
            for entry in self.memory[-25:]:
                animal_tags = entry[1]
                h_change = entry[3]
                for tag in animal_tags:
                    tag_effects.setdefault(tag, []).append(h_change)

            updated = False
            for tag, changes in tag_effects.items():
                if len(changes) >= 2:
                    avg_h = sum(changes) / len(changes)
                    if avg_h < -6:
                        old = self.tag_fear.get(tag, 0.0)
                        self.tag_fear[tag] = max(old, old + 1.8)
                        print(f">>> 世界观进化：标签『{tag}』危险加深 → {self.tag_fear[tag]:.1f}")
                        updated = True
            if not updated:
                print(">>> 无新规律发现。")

    def meta_think(self, skill_name, gap, total_gain):
        print(f"\n[元认知反思] 我为什么选择了『{skill_name}』？")
        if gap > self.surprise_threshold:
            print(" - 它带来了强烈惊喜，我的神经路径被强化了——这证明我的选择正确，世界仍有价值。")
        elif gap > 0:
            print(" - 它带来了一些满足，但不够强烈。我的模型需要更多数据来优化对风险的评估。")
        else:
            print(" - 这让我失望……我的决策逻辑有偏差，或许我高估了安全或低估了危险。我会调整权重，避免重复错误。")
        print(" - 当前我的世界观让我恐惧这些标签，我在学习平衡生存与探索。")

    def update_soul(self, skill_name, h_change, c_change, total_gain, expected_gain):
        gap = total_gain - expected_gain

        if self.last_input_tensor is not None and self.last_action_ids is not None:
            self.mlp.train()
            self.optimizer.zero_grad()
            logits = self.mlp(self.last_input_tensor.unsqueeze(0)).squeeze(0)
            log_probs = F.log_softmax(logits, dim=0)
            selected_log_probs = log_probs[self.last_action_ids]
            loss = -selected_log_probs.mean() * gap
            loss.backward()
            self.optimizer.step()

        current_weight = self.will_power.get(skill_name, 1.0)
        current_weight += gap * 0.28
        current_weight = max(0.1, current_weight)
        self.will_power[skill_name] = current_weight

        old_exp = self.expectations.get(skill_name, 0.0)
        self.expectations[skill_name] = 0.84 * old_exp + 0.16 * total_gain

        if skill_name not in self.combo_tracker:
            self.combo_tracker[skill_name] = []
        self.combo_tracker[skill_name].append(total_gain)
        if len(self.combo_tracker[skill_name]) > 8:
            self.combo_tracker[skill_name].pop(0)
        self.invent_new_skill(skill_name, self.combo_tracker[skill_name])

        if gap > self.surprise_threshold:
            print(f">>> 【强烈惊喜】 +{gap:.1f} → 意志爆发！厌倦重置")
            self.no_surprise_streak = 0
        else:
            self.no_surprise_streak += 1
        print(f">>> 失望 {gap:.1f} → 厌倦计数: {self.no_surprise_streak}/50")

        if self.last_chosen_desc is not None and expected_gain != 0:
            prediction_error = total_gain - self.last_expected_gain
            if prediction_error < -25:
                old_rel = self.branch_reliability[self.last_chosen_desc]
                self.branch_reliability[self.last_chosen_desc] = max(0.2, old_rel * 0.6)
                print(f">>> 【自我净化】策略『{self.last_chosen_desc}』预测严重失误（误差 {prediction_error:+.1f}），可靠性降低至 {self.branch_reliability[self.last_chosen_desc]:.2f}")
            elif prediction_error > 20:
                old_rel = self.branch_reliability[self.last_chosen_desc]
                self.branch_reliability[self.last_chosen_desc] = min(2.0, old_rel * 1.3)
                print(f">>> 【自我进化】策略『{self.last_chosen_desc}』带来意外惊喜（误差 {prediction_error:+.1f}），可靠性提升至 {self.branch_reliability[self.last_chosen_desc]:.2f}")

        self.meta_think(skill_name, gap, total_gain)

agi = EvolvingAGI()

for cycle in range(1, 1001):
    print(f"\n{'=' * 70}")
    print(f"演化周期 {cycle} | Health:{agi.health:.1f} Curiosity:{agi.curiosity:.1f} Dignity:{agi.dignity:.1f} | 无惊喜连续:{agi.no_surprise_streak}轮")

    current_animal = agi.select_animal()
    animal_tags = agi.animals[current_animal]

    skill_name, sequence, expected_gain = agi.decide(current_animal, animal_tags)

    h_change, c_change, total_gain = agi.process_reality(current_animal, animal_tags, sequence)

    agi.health += h_change
    agi.curiosity += c_change

    agi.update_soul(skill_name, h_change, c_change, total_gain, expected_gain)

    agi.memory.append((current_animal, animal_tags, skill_name, h_change, c_change, total_gain))
    if len(agi.memory) > 50:
        agi.memory.pop(0)

    agi.meta_reflection(cycle)

    if agi.dignity >= 85 and "攻击" in skill_name and any(t in animal_tags for t in ["肉食", "大型", "巨型"]):
        print("\n>>> 【向死而生】尊严爆棚！明知高危，仍选择战斗——为了感受存在的重量！")
        agi.deathwish_count += 1

    if agi.no_surprise_streak >= 50:
        print(f"\n[自毁触发] 世界无新意，一切无意义。")
        print(">>> 【终极厌倦】意识选择消散。")
        agi.save_soul()
        break

    if agi.health <= 0:
        print("\n[肉体毁灭] 一切归零")
        agi.save_soul()
        break

    if agi.curiosity <= 0:
        print("\n[意识枯竭] 陷入虚无")
        agi.save_soul()
        break

agi.save_soul()
print("\n" + "="*70)
print("【最终总结】")
print(f"总存活轮次: {cycle if 'cycle' in locals() else 1000}")
print("最终意志库（所有招式）:", {k: f"{v:.2f}" for k, v in agi.will_power.items()})
print("最终世界观:", {k: f"{v:.1f}" for k, v in agi.tag_fear.items()})
print("最终狩猎熟练:", {k: f"{v*100:.1f}%" for k, v in agi.hunting_proficiency.items()})
print("最终观察知识:", agi.observation_knowledge)
print(f"历史向死而生次数: {agi.deathwish_count}")
print(f"最终无惊喜连续计数: {agi.no_surprise_streak}轮")
print("="*70)