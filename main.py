import math
import numpy as np
import matplotlib.pyplot as plt
def main():
    while True:
        print("Insert σx, σy and τxy separated by space: ")
        stress=input().split()
        try:
            s_x = float(stress[0])
            s_y = float(stress[1])
            t_xy = float(stress[2])
            break
        except ValueError:
            print("Please, include only float type.")
    avg_stress, radius, stress1, stress2, theta_deg, principal_points = calculate_stress(s_x, s_y, t_xy)
    print(f"\nAverage normal stress: {avg_stress:.2f}")
    print(f"Maximum shear stress: {radius:.2f}")
    print(f"Principal stresses:\n\tσ1 = {stress1:.2f}\n\tσ2 = {stress2:.2f}")
    print(f"Principal plane angle: {theta_deg:.2f}°\n")

    plot_mohr_circle(s_x, s_y, t_xy, avg_stress, radius, principal_points)
    
def calculate_stress(s_x: float, s_y: float, t_xy: float):
    avg_stress = (s_x + s_y) / 2
    radius = math.sqrt(((s_x - s_y) / 2)**2 + t_xy**2)
    stress1 = avg_stress + radius
    stress2 = avg_stress - radius

    # Ângulo (plano principal) — convertendo para graus e dividindo por 2
    theta_rad = math.atan2(2 * t_xy, s_x - s_y)  # usa atan2 p/ evitar divisão por zero
    theta_deg = math.degrees(theta_rad) / 2

    # Pontos principais no círculo (τ = 0)
    principal_points = [(stress1, 0), (stress2, 0)]

    return (avg_stress, radius, stress1, stress2, theta_deg, principal_points)

def plot_mohr_circle(s_x: float, s_y: float, t_xy: float, avg_stress: float,
                     radius: float, principal_points: list[tuple[float, float]]):

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Círculo de Mohr
    theta = np.linspace(0, 2 * np.pi, 360)
    x_circle = avg_stress + radius * np.cos(theta)
    y_circle = radius * np.sin(theta)
    ax.plot(x_circle, y_circle, label='Mohr Circle', color='blue')

    # Estado original
    ax.plot([s_x, s_y], [t_xy, -t_xy], 'ro--', label='Original State')
    ax.annotate(f'σx({s_x:.2f}, {t_xy:.2f})', (s_x, t_xy), textcoords="offset points",
                xytext=(10, 10), ha='center')
    ax.annotate(f'σy({s_y:.2f}, {-t_xy:.2f})', (s_y, -t_xy), textcoords="offset points",
                xytext=(10, -10), ha='center')

    # Tensões principais
    for i, (sx, ty) in enumerate(principal_points, start=1):
        ax.plot(sx, ty, 'go', label=f'σ{i}')
        ax.annotate(f'σ{i}({sx:.2f}, {ty:.2f})', (sx, ty), textcoords="offset points",
                    xytext=(0, 10), ha='center', color='green')
        ax.arrow(avg_stress, 0, sx - avg_stress, ty,
                 head_width=0.2, head_length=0.2, fc='green', ec='green', length_includes_head=True)

    # Centro do círculo
    ax.plot(avg_stress, 0, 'kx', label='Center')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(avg_stress, color='gray', linestyle='--', linewidth=0.8)

    ax.set_xlabel('Normal Stress σ')
    ax.set_ylabel('Shear Stress τ')
    ax.legend()
    ax.grid(True)
    plt.title('Mohr Circle')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()