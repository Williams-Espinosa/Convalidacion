# 🌀 Teorema de Gauss-Ostrogradsky (Teorema de la Divergencia)

Este proyecto presenta una investigación profunda y una verificación computacional del Teorema de Gauss-Ostrogradsky. El trabajo demuestra la relación fundamental entre la integral de flujo de un campo vectorial sobre una superficie cerrada y la integral de la divergencia del campo sobre el volumen encerrado.

## 📐 Fundamentos del Teorema

El teorema se expresa matemáticamente como:

$$\iiint_{V} \nabla \cdot \mathbf{F} \, dV = \oiint_{\partial V} \mathbf{F} \cdot \mathbf{n} \, dS$$

### Casos de Estudio Verificados
En este proyecto se analizaron tres geometrías distintas con sus respectivos campos vectoriales:
1.  **Esfera:** Campo radial $\mathbf{F} = (x, y, z)$.
2.  **Cubo:** Campo cuadrático $\mathbf{F} = (x^2, y^2, z^2)$.
3.  **Cilindro:** Campo compuesto $\mathbf{F} = (x, y, z^2)$.

---

## 🐍 Implementación en Python

Se desarrolló un script de validación utilizando librerías científicas para comparar los resultados analíticos contra los numéricos:

* **NumPy:** Para el manejo de vectores y arreglos.
* **SciPy (integrate):** Para el cálculo de integrales triples (volumen) y dobles (superficie) mediante cuadraturas adaptativas.
* **Matplotlib:** Para la visualización 3D de las regiones y la generación de gráficas comparativas que verifican que la diferencia entre ambas integrales es prácticamente nula.

---

## 📊 Conclusiones del Análisis
* Se confirmó que el teorema permite simplificar cálculos de flujo complejos convirtiéndolos en integrales de volumen más sencillas.
* La precisión obtenida en la simulación numérica fue del orden de $10^{-14}$, validando la exactitud del modelo implementado.

---

## 📂 Archivos en esta Carpeta
* `Gauss.Ostrogradsky.WilliamsEspinosaLopez.251185.pdf`: Reporte de investigación detallado con demostraciones matemáticas.
* `Gauss.Ostrogradsky.WilliamsEspinosaLopez.251185.py`: Script de Python con las simulaciones y gráficas.

---
**Autor:** Williams Espinosa López
**Matrícula:** 251185
**Asignatura:** Cálculo Integral