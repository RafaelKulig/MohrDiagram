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
    maindata=CalculateStress(s_x,s_y,t_xy)
    print(f"Average normal stress: {maindata[0]:.2f}\nMaximum shear: {maindata[1]:.2f}\nPrincipal stress:\n\t1:{maindata[2]:.2f}\n\t2:{maindata[3]:.2f}\nMain plane: {maindata[4]/2:.2f}")
    PlotMohrCircle(s_x, s_y, t_xy)

def CalculateStress(s_x:float,s_y:float,t_xy:float):
    avg_stress=(s_x+s_y)/2
    radius=pow(pow((s_x-s_y)/2,2)+t_xy**2,0.5)
    stress1=avg_stress+radius
    stress2=avg_stress-radius
    theta_2=rad2deg(math.atan(2*t_xy/(s_x-s_y)))
    return(avg_stress,radius,stress1,stress2,theta_2)

def PlotMohrCircle(s_x, s_y, t_xy):
    avg_stress = (s_x + s_y) / 2
    radius = math.sqrt(((s_x - s_y) / 2)**2 + t_xy**2)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Gerar pontos do círculo
    theta = np.linspace(0, 2 * np.pi, 360)
    x_circle = avg_stress + radius * np.cos(theta)
    y_circle = radius * np.sin(theta)

    # Plotar o círculo
    ax.plot(x_circle, y_circle, label='Círculo de Mohr')
    ax.plot([s_x, s_y], [t_xy, -t_xy], 'ro--', label='Estado de tensão')
    ax.plot(avg_stress, 0, 'kx', label='Centro')

    # Adicionar anotações
    ax.annotate('σx', (s_x, t_xy), textcoords="offset points", xytext=(10,10), ha='center')
    ax.annotate('σy', (s_y, -t_xy), textcoords="offset points", xytext=(10,-10), ha='center')

    # Eixos
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(avg_stress, color='gray', linestyle='--', linewidth=0.8)

    ax.set_xlabel('Tensão normal σ')
    ax.set_ylabel('Tensão de cisalhamento τ')
    ax.legend()
    ax.grid(True)
    plt.title('Círculo de Mohr')
    plt.show()

def rad2deg(angle):
    return angle*180/math.pi
if __name__=="__main__":
    main()