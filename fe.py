import math

# Parameters
# u = 1.5
# d = 1 / u
# T = 5
# r = 0  # risk-free rate
# K = 31
# S0 = 36

# # Risk-neutral probability
# p = (math.exp(r) - d) / (u - d)

# # Build binomial tree of stock prices
# stock_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
# for i in range(T + 1):
#     for j in range(i + 1):
#         stock_tree[j][i] = S0 * (u ** j) * (d ** (i - j))

# # Initialize option tree
# option_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]

# # Terminal payoff for American call
# for j in range(T + 1):
#     option_tree[j][T] = max(stock_tree[j][T] - K, 0)

# # Backward induction for American call option
# for i in range(T - 1, -1, -1):
#     for j in range(i + 1):
#         exercise = max(stock_tree[j][i] - K, 0)
#         hold = math.exp(-r) * (p * option_tree[j + 1][i + 1] + (1 - p) * option_tree[j][i + 1])
#         option_tree[j][i] = max(exercise, hold)

# # American call option price at t=0
# option_price = option_tree[0][0]
# print(f"Option Price: {option_price}")


# import numpy as np

# # Given parameters
# S0 = 36
# K = 31
# r = 0
# T = 5
# N = 5
# u = 1.5
# d = 1 / u
# dt = T / N

# # Risk-neutral probability
# p = (np.exp(r * dt) - d) / (u - d)
# q = 1 - p

# # Initialize the stock price tree
# stock_tree = np.zeros((N + 1, N + 1))
# for i in range(N + 1):
#     for j in range(i + 1):
#         stock_tree[i, j] = S0 * (u ** j) * (d ** (i - j))

# # Initialize the option value tree
# option_tree = np.zeros((N + 1, N + 1))

# # At maturity (T=5), the option value is the intrinsic value
# for j in range(N + 1):
#     option_tree[N, j] = max(0, stock_tree[N, j] - K)

# # Work backwards to calculate American call option values at each node
# for i in range(N - 1, -1, -1):
#     for j in range(i + 1):
#         # Value if the option is held (continuation value)
#         continuation_value = np.exp(-r * dt) * (p * option_tree[i + 1, j + 1] + q * option_tree[i + 1, j])
        
#         # Value if the option is exercised immediately (intrinsic value)
#         intrinsic_value = max(0, stock_tree[i, j] - K)
        
#         # The American option value is the maximum of the two
#         option_tree[i, j] = max(continuation_value, intrinsic_value)

# # The price of the option is the value at the root of the tree (t=0)
# option_price = option_tree[0, 0]

# print(f"Option Price: {option_price:.2f}")

# Parameters for the American call option
# u = 1.2
# d = 1 / u
# T = 5
# r = 0
# K = 45
# S0 = 45

# # Risk-neutral probability
# p = (math.exp(r) - d) / (u - d)

# # Function to compute stock price at a node (j up moves, i time step)
# def stock_price(S0, u, d, j, i):
#     return S0 * (u ** j) * (d ** (i - j))

# # Function to compute American call price from a given node
# def american_call_price_from_node(S_start, u, d, r, K, T_remaining, p):
#     option = [0] * (T_remaining + 1)
#     for j in range(T_remaining + 1):
#         S = S_start * (u ** j) * (d ** (T_remaining - j))
#         option[j] = max(S - K, 0)
#     for i in range(T_remaining - 1, -1, -1):
#         for j in range(i + 1):
#             S = S_start * (u ** j) * (d ** (i - j))
#             exercise = max(S - K, 0)
#             hold = math.exp(-r) * (p * option[j + 1] + (1 - p) * option[j])
#             option[j] = max(exercise, hold)
#     return option[0]

# # Compute stock prices at t=2 for dd (j=0) and du (j=1)
# S_dd = stock_price(S0, u, d, 0, 2)
# S_du = stock_price(S0, u, d, 1, 2)

# # Compute option values starting from these nodes with 3 steps remaining
# V_dd = american_call_price_from_node(S_dd, u, d, r, K, 3, p)
# V_du = american_call_price_from_node(S_du, u, d, r, K, 3, p)

# # Compute delta at node (dd)
# delta_dd = (V_du - V_dd) / (S_du - S_dd)
# print(delta_dd)


# import numpy as np

# # Given parameters
# S0 = 45
# K = 45
# r = 0
# T = 5
# N = 5
# u = 1.2
# d = 1/u
# dt = T/N
# p = (np.exp(r * dt) - d) / (u - d)

# # Initialize the stock price tree
# stock_tree = np.zeros((N + 1, N + 1))
# stock_tree[0, 0] = S0
# for i in range(1, N + 1):
#     stock_tree[i, 0] = stock_tree[i - 1, 0] * d
#     for j in range(1, i + 1):
#         stock_tree[i, j] = stock_tree[i - 1, j - 1] * u

# # Initialize the option value tree
# option_tree = np.zeros((N + 1, N + 1))

# # At maturity (T=5), the option value is the payoff or intrinsic value
# # For an American call with r=0 and no dividends, early exercise is never optimal.
# # The value is the same as a European call.
# for j in range(N + 1):
#     option_tree[N, j] = max(0, stock_tree[N, j] - K)

# # Work backwards to calculate option values at each node
# for i in range(N - 1, -1, -1):
#     for j in range(i + 1):
#         european_value = np.exp(-r * dt) * (p * option_tree[i + 1, j + 1] + (1 - p) * option_tree[i + 1, j])
#         american_value = max(european_value, stock_tree[i, j] - K)
#         option_tree[i, j] = american_value

# # The question asks for delta at the dd node at time step 2 (Δ_2^dd)
# # This corresponds to the node at (i=2, j=0) in our tree where j is the number of up moves
# # The stock price at this node is S_0 * d^2
# # The "up" node from this point is at (i=3, j=1), with stock price S_0 * d^2 * u
# # The "down" node from this point is at (i=3, j=0), with stock price S_0 * d^3

# # Let's find the required option values from the tree
# V_2_dd = option_tree[2, 0]
# V_3_ddu = option_tree[3, 1]
# V_3_ddd = option_tree[3, 0]

# # Delta is calculated as: (V_up - V_down) / (S_up - S_down)
# # In our case, for Δ_2^dd, the "up" is the ddu path and "down" is the ddd path.
# S_2_dd = stock_tree[2, 0]
# S_3_ddu = stock_tree[3, 1]
# S_3_ddd = stock_tree[3, 0]

# delta_2_dd = (V_3_ddu - V_3_ddd) / (S_3_ddu - S_3_ddd)

# # Print the required values for calculation
# print(f"p: {p:.4f}")
# print(f"S_3_ddu: {S_3_ddu:.4f}")
# print(f"S_3_ddd: {S_3_ddd:.4f}")
# print(f"V_3_ddu: {V_3_ddu:.4f}")
# print(f"V_3_ddd: {V_3_ddd:.4f}")
# print(f"Delta_2_dd: {delta_2_dd:.4f}")

# Parameters for American put option
# u = 1.5
# d = 1 / u
# T = 50
# r = 0
# K = 31
# S0 = 36

# # Risk-neutral probability
# p = (math.exp(r) - d) / (u - d)

# # Initialize stock price tree
# stock_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
# stock_tree[0][0] = S0
# for i in range(1, T + 1):
#     stock_tree[0][i] = stock_tree[0][i - 1] * d
#     for j in range(1, i + 1):
#         stock_tree[j][i] = stock_tree[j - 1][i - 1] * u

# # Initialize option value tree
# option_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
# for j in range(T + 1):
#     option_tree[j][T] = max(K - stock_tree[j][T], 0)

# # Backward induction for American put
# for i in range(T - 1, -1, -1):
#     for j in range(i + 1):
#         exercise = max(K - stock_tree[j][i], 0)
#         hold = math.exp(-r) * (p * option_tree[j + 1][i + 1] + (1 - p) * option_tree[j][i + 1])
#         option_tree[j][i] = max(exercise, hold)

# # Price of American put at t=0
# american_put_price = option_tree[0][0]
# american_put_price
# print(f"American Put Option Price: {american_put_price:.2f}")

# import numpy as np

# # Given parameters
# S0 = 36
# K = 31
# r = 0
# T = 50
# N = 50
# u = 1.5
# d = 1 / u
# dt = T / N

# # Risk-neutral probability
# p = (np.exp(r * dt) - d) / (u - d)

# # Initialize the stock price tree
# stock_tree = np.zeros((N + 1, N + 1))
# for i in range(N + 1):
#     for j in range(i + 1):
#         stock_tree[i, j] = S0 * (u ** j) * (d ** (i - j))

# # Initialize the option value tree
# option_tree = np.zeros((N + 1, N + 1))

# # At maturity (T=50), the option value is the intrinsic value
# for j in range(N + 1):
#     option_tree[N, j] = max(0, K - stock_tree[N, j])

# # Work backwards to calculate option values at each node
# for i in range(N - 1, -1, -1):
#     for j in range(i + 1):
#         # Value if the option is held (continuation value)
#         continuation_value = np.exp(-r * dt) * (p * option_tree[i + 1, j + 1] + (1 - p) * option_tree[i + 1, j])
        
#         # Value if the option is exercised immediately (intrinsic value)
#         intrinsic_value = max(0, K - stock_tree[i, j])
        
#         # The American option value is the maximum of the two
#         option_tree[i, j] = max(continuation_value, intrinsic_value)

# # The price of the option is the value at the root of the tree (t=0)
# option_price = option_tree[0, 0]

# print(f"p: {p}")
# print(f"Option Price: {option_price}")

# Parameters for this American put option
# u = 1.2
# d = 1 / u
# T = 50
# r = 0
# K = 45
# S0 = 45

# # Risk-neutral probability
# p = (math.exp(r) - d) / (u - d)

# # Initialize stock price tree
# stock_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
# stock_tree[0][0] = S0
# for i in range(1, T + 1):
#     stock_tree[0][i] = stock_tree[0][i - 1] * d
#     for j in range(1, i + 1):
#         stock_tree[j][i] = stock_tree[j - 1][i - 1] * u

# # Initialize option value tree
# option_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
# for j in range(T + 1):
#     option_tree[j][T] = max(K - stock_tree[j][T], 0)

# # Backward induction
# for i in range(T - 1, -1, -1):
#     for j in range(i + 1):
#         exercise = max(K - stock_tree[j][i], 0)
#         hold = math.exp(-r) * (p * option_tree[j + 1][i + 1] + (1 - p) * option_tree[j][i + 1])
#         option_tree[j][i] = max(exercise, hold)

# # Final price
# american_put_price = option_tree[0][0]
# american_put_price
# print(f"American Put Option Price: {american_put_price:.2f}")


# Parameters for the American put option
u = 1.5
d = 1 / u
T = 5
r = 0
K = 45
S0 = 45

# Risk-neutral probability
p = (math.exp(r) - d) / (u - d)

# Build binomial tree of stock prices
stock_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
stock_tree[0][0] = S0
for i in range(1, T + 1):
    stock_tree[0][i] = stock_tree[0][i - 1] * d
    for j in range(1, i + 1):
        stock_tree[j][i] = stock_tree[j - 1][i - 1] * u

# Initialize option price tree
option_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]
for j in range(T + 1):
    option_tree[j][T] = max(K - stock_tree[j][T], 0)

# Backward induction for American put
for i in range(T - 1, -1, -1):
    for j in range(i + 1):
        exercise = max(K - stock_tree[j][i], 0)
        hold = math.exp(-r) * (p * option_tree[j + 1][i + 1] + (1 - p) * option_tree[j][i + 1])
        option_tree[j][i] = max(exercise, hold)

# Compute Delta at time step 1, up move
V_1_u = option_tree[1][1]
V_1_d = option_tree[0][1]
S_1_u = stock_tree[1][1]
S_1_d = stock_tree[0][1]

delta_u_1 = (V_1_u - V_1_d) / (S_1_u - S_1_d)
delta_u_1
print(f"Delta at time step 1, up move: {delta_u_1:.4f}")