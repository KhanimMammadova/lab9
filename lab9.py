# Başlanğıc yaxınlaşma
x0 = 1.0
tol = 1e-6  # dayandırma üçün tolerantlıq
max_iter = 100  # maksimum iterasiya sayı

print(f"x0 = {x0:.6f}")

for i in range(1, max_iter + 1):
    x1 = (x0 + 2) ** (1/5)
    print(f"x{i} = (x{i-1} + 2)^(1/5) = {x1:.6f}")
    
    if abs(x1 - x0) < tol:
        print(f"\nYakın kök c₀ təxminən: {x1:.6f}")
        break

    x0 = x1
