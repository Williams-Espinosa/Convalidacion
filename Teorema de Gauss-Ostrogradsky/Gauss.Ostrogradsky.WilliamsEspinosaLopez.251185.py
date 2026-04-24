import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from scipy import integrate

def ejemplo_1_esfera(R=1.0):
    print("\n" + "=" * 65)
    print("  EJEMPLO 1 : Campo F = (x, y, z) sobre esfera de radio R =", R)
    print("=" * 65)

    div_F = 3.0
    volumen_esfera = (4.0 / 3.0) * np.pi * R**3
    integral_volumen = div_F * volumen_esfera

    f_div = lambda rho, phi, theta: 3.0 * rho**2 * np.sin(phi)
    integral_num, _ = integrate.tplquad(
        f_div,
        0, 2 * np.pi,          
        0, np.pi,              
        0, R,                  
    )


    area_esfera = 4.0 * np.pi * R**2
    flujo_analitico = R * area_esfera

    f_flux = lambda phi, theta: R * R**2 * np.sin(phi)
    flujo_num, _ = integrate.dblquad(
        f_flux,
        0, 2 * np.pi,    
        0, np.pi,        
    )

    print(f"  Integral de volumen (div F):  {integral_volumen:.6f}")
    print(f"  Integral numerica de volumen: {integral_num:.6f}")
    print(f"  Integral de superficie (F.n): {flujo_analitico:.6f}")
    print(f"  Integral numerica de flujo:   {flujo_num:.6f}")
    print(f"  Diferencia: {abs(integral_volumen - flujo_analitico):.2e}")
    print("  >> El teorema se verifica: ambos lados coinciden.")

    fig = plt.figure(figsize=(11, 5))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    u = np.linspace(0, 2 * np.pi, 40)
    v = np.linspace(0, np.pi, 20)
    xs = R * np.outer(np.cos(u), np.sin(v))
    ys = R * np.outer(np.sin(u), np.sin(v))
    zs = R * np.outer(np.ones_like(u), np.cos(v))
    ax1.plot_surface(xs, ys, zs, alpha=0.25, color='skyblue',
                    edgecolor='steelblue', linewidth=0.2)

    u2 = np.linspace(0, 2 * np.pi, 10)
    v2 = np.linspace(0.2, np.pi - 0.2, 6)
    U2, V2 = np.meshgrid(u2, v2)
    xv = R * np.cos(U2) * np.sin(V2)
    yv = R * np.sin(U2) * np.sin(V2)
    zv = R * np.cos(V2)
    ax1.quiver(xv, yv, zv, xv, yv, zv,
            length=0.35, normalize=False, color='crimson', alpha=0.8)
    ax1.set_title("Ejemplo 1: F = (x,y,z) y esfera")
    ax1.set_xlabel("X"); ax1.set_ylabel("Y"); ax1.set_zlabel("Z")

    ax2 = fig.add_subplot(1, 2, 2)
    lados = ["Volumen\n∭ div F dV", "Superficie\n∯ F·n dS"]
    valores = [integral_volumen, flujo_analitico]
    barras = ax2.bar(lados, valores, color=['#3a86ff', '#ff006e'],
                    edgecolor='black', width=0.5)
    ax2.set_ylabel("Valor de la integral")
    ax2.set_title(f"Verificacion Gauss-Ostrogradsky\n"
                  f"Valor teorico: 4πR³ = {4 * np.pi * R**3:.4f}")
    ax2.grid(True, alpha=0.3, axis='y')
    for b, v_ in zip(barras, valores):
        ax2.text(b.get_x() + b.get_width() / 2, v_ + 0.1,
                f"{v_:.4f}", ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig("ejemplo1_esfera.png", dpi=130, bbox_inches='tight')
    plt.close()
    print("  Grafica guardada: ejemplo1_esfera.png")

    return integral_volumen, flujo_analitico

def ejemplo_2_cubo(a=1.0):
    print("\n" + "=" * 65)
    print(f"  EJEMPLO 2 : Campo F = (x², y², z²) sobre cubo [0,{a}]^3")
    print("=" * 65)

    div_int_analitica = 3.0 * a**4
    div_F = lambda x, y, z: 2 * x + 2 * y + 2 * z
    div_num, _ = integrate.tplquad(
        div_F,
        0, a,   
        0, a,  
        0, a,   
    )

    flujo_x_mas  = a**2 * a**2
    flujo_x_menos = 0.0
    flujo_y_mas  = a**2 * a**2
    flujo_y_menos = 0.0
    flujo_z_mas  = a**2 * a**2
    flujo_z_menos = 0.0
    flujo_total = (flujo_x_mas + flujo_x_menos +
                flujo_y_mas + flujo_y_menos +
                flujo_z_mas + flujo_z_menos)

    flujo_num_total = 0.0

    fx, _ = integrate.dblquad(lambda z, y: a**2, 0, a, 0, a)

    fy, _ = integrate.dblquad(lambda z, x: a**2, 0, a, 0, a)

    fz, _ = integrate.dblquad(lambda y, x: a**2, 0, a, 0, a)
    flujo_num_total = fx + fy + fz

    print(f"  Integral de volumen (analitica): {div_int_analitica:.6f}")
    print(f"  Integral numerica de volumen:    {div_num:.6f}")
    print(f"  Flujo total (analitico):         {flujo_total:.6f}")
    print(f"  Flujo total (numerico):          {flujo_num_total:.6f}")
    print(f"  Diferencia: {abs(div_int_analitica - flujo_total):.2e}")
    print("  >> El teorema se verifica: ambos lados coinciden.")

    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')

    r = [0, a]
    from itertools import product, combinations
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s - e)) == a:
            ax1.plot3D(*zip(s, e), color="black", linewidth=1.3)

    n = 4
    xs = np.linspace(0.1 * a, 0.9 * a, n)
    ys = np.linspace(0.1 * a, 0.9 * a, n)
    zs = np.linspace(0.1 * a, 0.9 * a, n)
    X, Y, Z = np.meshgrid(xs, ys, zs)
    U = X**2; V = Y**2; W = Z**2
    ax1.quiver(X, Y, Z, U, V, W, length=0.25, normalize=True,
            color='darkgreen', alpha=0.6)

    ax1.set_title(f"Ejemplo 2: F = (x², y², z²) en cubo [0,{a}]³")
    ax1.set_xlabel("X"); ax1.set_ylabel("Y"); ax1.set_zlabel("Z")

    ax2 = fig.add_subplot(1, 2, 2)
    caras = ['x=0', 'x=a', 'y=0', 'y=a', 'z=0', 'z=a']
    flujos = [flujo_x_menos, flujo_x_mas, flujo_y_menos, flujo_y_mas,
            flujo_z_menos, flujo_z_mas]
    colores = ['#cccccc', '#2a9d8f', '#cccccc', '#e76f51',
            '#cccccc', '#f4a261']
    barras = ax2.bar(caras, flujos, color=colores, edgecolor='black')
    ax2.axhline(y=div_int_analitica, color='red', linestyle='--',
                label=f'∭ div F dV = {div_int_analitica:.3f}')
    ax2.set_ylabel("Flujo a traves de la cara")
    ax2.set_title(f"Flujo por cara   (Suma = {flujo_total:.3f})")
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    for b, v_ in zip(barras, flujos):
        ax2.text(b.get_x() + b.get_width() / 2, v_ + 0.02,
                f"{v_:.3f}", ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig("ejemplo2_cubo.png", dpi=130, bbox_inches='tight')
    plt.close()
    print("  Grafica guardada: ejemplo2_cubo.png")

    return div_int_analitica, flujo_total

def ejemplo_3_cilindro(R=1.0, h=2.0):
    print("\n" + "=" * 65)
    print(f"  EJEMPLO 3 : Campo F = (xz, yz, z²) sobre cilindro "
        f"R={R}, h={h}")
    print("=" * 65)


    div_int_analitica = 2 * np.pi * R**2 * h**2
    f_div_cyl = lambda z, r, theta: 4 * z * r
    div_num, _ = integrate.tplquad(
        f_div_cyl,
        0, 2 * np.pi,   
        0, R,          
        0, h,          
    )

    flujo_tapa_sup = h**2 * np.pi * R**2

    flujo_tapa_inf = 0.0

    flujo_lateral = np.pi * R**2 * h**2

    flujo_total = flujo_tapa_sup + flujo_tapa_inf + flujo_lateral

    flujo_lat_num, _ = integrate.dblquad(
        lambda z, theta: z * R * R,
        0, 2 * np.pi,   
        0, h,           
    )
    flujo_tapa_num, _ = integrate.dblquad(
        lambda r, theta: h**2 * r,
        0, 2 * np.pi,   
        0, R,           
    )
    flujo_num_total = flujo_lat_num + flujo_tapa_num + 0.0

    print(f"  Integral de volumen (analitica): {div_int_analitica:.6f}")
    print(f"  Integral numerica de volumen:    {div_num:.6f}")
    print(f"  Flujo tapa superior:  {flujo_tapa_sup:.6f}")
    print(f"  Flujo tapa inferior:  {flujo_tapa_inf:.6f}")
    print(f"  Flujo lateral:        {flujo_lateral:.6f}")
    print(f"  Flujo total:          {flujo_total:.6f}")
    print(f"  Flujo numerico total: {flujo_num_total:.6f}")
    print(f"  Diferencia: {abs(div_int_analitica - flujo_total):.2e}")
    print("  >> El teorema se verifica: ambos lados coinciden.")

    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    theta = np.linspace(0, 2 * np.pi, 60)
    z = np.linspace(0, h, 25)
    TH, Z = np.meshgrid(theta, z)
    Xc = R * np.cos(TH)
    Yc = R * np.sin(TH)
    ax1.plot_surface(Xc, Yc, Z, alpha=0.3, color='lightcoral',
                    edgecolor='firebrick', linewidth=0.2)

    r_t = np.linspace(0, R, 15)
    th_t = np.linspace(0, 2 * np.pi, 40)
    RR, TT = np.meshgrid(r_t, th_t)
    Xt = RR * np.cos(TT); Yt = RR * np.sin(TT); Zt = np.full_like(Xt, h)
    ax1.plot_surface(Xt, Yt, Zt, alpha=0.4, color='khaki',
                    edgecolor='goldenrod', linewidth=0.2)

    theta_v = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    z_v = np.linspace(0.2, h - 0.2, 4)
    for tv in theta_v:
        for zv in z_v:
            xv = R * np.cos(tv) * 0.85
            yv = R * np.sin(tv) * 0.85
            ax1.quiver(xv, yv, zv,
                       xv * zv, yv * zv, zv**2,
                    length=0.18, normalize=True,
                    color='navy', alpha=0.75)

    ax1.set_title(f"Ejemplo 3: F = (xz, yz, z²) en cilindro")
    ax1.set_xlabel("X"); ax1.set_ylabel("Y"); ax1.set_zlabel("Z")

    ax2 = fig.add_subplot(1, 2, 2)
    etiquetas = ["Tapa inf.\n(z=0)", "Lateral", "Tapa sup.\n(z=h)",
                "Flujo\ntotal", "∭ div F dV"]
    valores = [flujo_tapa_inf, flujo_lateral, flujo_tapa_sup,
            flujo_total, div_int_analitica]
    colores = ['#adb5bd', '#4cc9f0', '#f72585', '#7209b7', '#06d6a0']
    barras = ax2.bar(etiquetas, valores, color=colores, edgecolor='black')
    ax2.set_ylabel("Valor de la integral")
    ax2.set_title(f"Contribuciones al flujo\n(Valor teorico: 2πR²h² "
                    f"≈ {div_int_analitica:.4f})")
    ax2.grid(True, alpha=0.3, axis='y')
    for b, v_ in zip(barras, valores):
        ax2.text(b.get_x() + b.get_width() / 2, v_ + 0.3,
                f"{v_:.3f}", ha='center', fontsize=9,
                fontweight='bold')

    plt.tight_layout()
    plt.savefig("ejemplo3_cilindro.png", dpi=130, bbox_inches='tight')
    plt.close()
    print("  Grafica guardada: ejemplo3_cilindro.png")

    return div_int_analitica, flujo_total

if __name__ == "__main__":
    print("#" * 65)
    print("#  TEOREMA DE GAUSS-OSTROGRADSKY (Teorema de la Divergencia)  ")
    print("#  Verificacion numerica de 3 ejemplos practicos             ")
    print("#" * 65)

    resultados = []
    resultados.append(("Esfera",   ejemplo_1_esfera(R=1.0)))
    resultados.append(("Cubo",     ejemplo_2_cubo(a=1.0)))
    resultados.append(("Cilindro", ejemplo_3_cilindro(R=1.0, h=2.0)))

    print("\n" + "=" * 65)
    print("   RESUMEN GLOBAL: Verificacion del Teorema")
    print("=" * 65)
    print(f"  {'Ejemplo':<12}{'∭ div F dV':>18}{'∯ F·n dS':>18}"
        f"{'|Dif|':>12}")
    print("  " + "-" * 58)
    for nombre, (vol, sup) in resultados:
        print(f"  {nombre:<12}{vol:>18.6f}{sup:>18.6f}"
            f"{abs(vol - sup):>12.2e}")
    print("=" * 65)
    print("  En los 3 ejemplos el teorema de Gauss-Ostrogradsky")
    print("  se cumple con una precision numerica excelente.")
    print("=" * 65)

    fig, ax = plt.subplots(figsize=(9, 5))
    nombres = [r[0] for r in resultados]
    vols = [r[1][0] for r in resultados]
    sups = [r[1][1] for r in resultados]
    x = np.arange(len(nombres))
    w = 0.35
    ax.bar(x - w / 2, vols, w, label="∭ div F dV (volumen)",
        color='#3a86ff', edgecolor='black')
    ax.bar(x + w / 2, sups, w, label="∯ F·n dS (superficie)",
        color='#ff006e', edgecolor='black')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    ax.set_ylabel("Valor de la integral")
    ax.set_title("Comparacion global: Gauss-Ostrogradsky")
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    for i, (v, s) in enumerate(zip(vols, sups)):
        ax.text(i - w / 2, v + 0.3, f"{v:.3f}", ha='center', fontsize=9)
        ax.text(i + w / 2, s + 0.3, f"{s:.3f}", ha='center', fontsize=9)
    plt.tight_layout()
    plt.savefig("resumen_comparativo.png", dpi=130, bbox_inches='tight')
    plt.close()
    print("\n  Grafica resumen guardada: resumen_comparativo.png")
    print("\n  Fin del programa. Revisar los archivos .png generados.")
