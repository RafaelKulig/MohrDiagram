import math
import numpy as np
import matplotlib.pyplot as plt
def main():
    while True:
        print("Insert \u03C3x, \u03C3y and \u03C4xy separeted by space: ", end="")
        stress=input().split(" ")
        try:
            s_x=float(stress[0])
            s_y=float(stress[1])
            t_xy=float(stress[2])
            break
        except:
            print("Please, include only float type.",end='\n')
    maindata = CalculateStress(s_x, s_y, t_xy)
    print(f"Average normal stress: {maindata[0]:.2f}")
    print(f"Maximum shear: {maindata[1]:.2f}")
    print(f"Principal stress:\n\t1: {maindata[2]:.2f}\n\t2: {maindata[3]:.2f}")
    print(f"Main plane angle: {maindata[4]:.2f}°")

    PlotMohrCircle(s_x, s_y, t_xy, maindata[0], maindata[1], maindata[5])
    
def CalculateStress(s_x: float, s_y: float, t_xy: float):
    avg_stress = (s_x + s_y) / 2
    radius = math.sqrt(((s_x - s_y) / 2)**2 + t_xy**2)
    stress1 = avg_stress + radius
    stress2 = avg_stress - radius

    # Ângulo (plano principal) — convertendo para graus e dividindo por 2
    theta_rad = math.atan2(2 * t_xy, s_x - s_y)  # usa atan2 p/ evitar divisão por zero
    theta_deg = rad2deg(theta_rad) / 2

    # Pontos principais no círculo (τ = 0)
    principal_points = [(stress1, 0), (stress2, 0)]

    return (avg_stress, radius, stress1, stress2, theta_deg, principal_points)

def PlotMohrCircle(s_x, s_y, t_xy, avg_stress, radius, principal_points):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Círculo
    theta = np.linspace(0, 2 * np.pi, 360)
    x_circle = avg_stress + radius * np.cos(theta)
    y_circle = radius * np.sin(theta)

    ax.plot(x_circle, y_circle)

    # Estado original
    ax.plot([s_x, s_y], [t_xy, -t_xy], 'ro--')
    ax.annotate(f'σx({s_x},{t_xy})', (s_x, t_xy), textcoords="offset points", xytext=(10,10), ha='center')
    ax.annotate(f'σy({s_y},{-t_xy})', (s_y, -t_xy), textcoords="offset points", xytext=(10,-10), ha='center')

    # Tensões principais
    for i, (sx, ty) in enumerate(principal_points, start=1):
        ax.plot(sx, ty, 'go')  # ponto verde
        ax.annotate(f'σ{i}({sx},{ty})', (sx, ty), textcoords="offset points", xytext=(0,10), ha='center', color='green')
        ax.arrow(avg_stress, 0, sx - avg_stress, ty, head_width=0.2, head_length=0.2, fc='green', ec='green', length_includes_head=True)

    # Centro
    ax.plot(avg_stress, 0, 'kx')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(avg_stress, color='gray', linestyle='--', linewidth=0.8)

    ax.set_xlabel('Normal Stress σ')
    ax.set_ylabel('Shear Stress τ')
    ax.legend()
    ax.grid(True)
    plt.title('Mohr Cicle')
    plt.show()

def rad2deg(angle):
    return angle*180/math.pi
if __name__=="__main__":
    main()