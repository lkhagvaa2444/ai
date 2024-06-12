# Define the functions
def g(x, y):
    return x * y

def f(g, z):
    return g * z

# Compute the gradients
def compute_gradients(x, y, z):
    g_result = g(x, y)
    f_result = f(g_result, z)

    df_dg = z
    df_dx = df_dg * y
    df_dy = df_dg * x
    df_dz = g_result

    return df_dx, df_dy, df_dz

# Example values
x = 2
y = 3
z = 4

# Compute gradients
df_dx, df_dy, df_dz = compute_gradients(x, y, z)

# Print results
print("Gradient with respect to x:", df_dx)
print("Gradient with respect to y:", df_dy)
print("Gradient with respect to z:", df_dz)
