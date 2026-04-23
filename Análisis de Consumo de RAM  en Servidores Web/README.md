# 📊 Análisis de Consumo de RAM en Servidores Web

Este proyecto presenta un estudio técnico sobre el comportamiento del consumo de memoria RAM en un servidor web durante un ciclo de 24 horas. El objetivo principal es modelar una ecuación matemática que permita predecir la carga del sistema considerando usuarios concurrentes y horas pico.

## 🧠 Modelado Matemático

Para representar la fluctuación de usuarios y el consumo de recursos, se definieron las siguientes variables y constantes:

* **Consumo base ($R_0$):** 2 GB (Sistema Operativo y servicios esenciales).
* **Consumo promedio por usuario ($r$):** 0.08 GB.
* **Carga base de usuarios ($U_0$):** 50 usuarios concurrentes.
* **Fluctuación máxima ($\Delta U$):** 30 usuarios adicionales en horas pico.

### Ecuación de Consumo
Utilizando una función periódica (seno) para simular los ciclos de tráfico diario , se obtuvo la siguiente función de consumo total $R(t)$ en GB:

$$R(t) = 6 + 2.4 \sin\left(\frac{\pi t}{12}\right)$$

Bajo este modelo, el consumo oscila dinámicamente entre un mínimo de **3.6 GB** y un máximo de **8.4 GB**.

---

## 📈 Aplicación de Cálculo Integral

Se utilizó la **integral definida** para calcular el **consumo acumulado de recursos** (en GB·h) durante la primera mitad del día (intervalo de $t=0$ a $t=12$ horas):

$$\int_{0}^{12} \left[ 6 + 2.4 \sin\left(\frac{\pi t}{12}\right) \right] dt$$

**Resultado del consumo acumulado:**
$$\approx 90.34 \text{ GB} \cdot h$$

---

## 📂 Archivos en esta Carpeta
* `PrimerActividad290126.pdf`: Documento técnico con la resolución y gráficas detalladas.
* `PrimerActividad290126.tex`: Código fuente en LaTeX utilizado para la documentación científica.

---
**Autor:** Williams Espinosa López 
**Docente:** Sirgei García Ballinas 
**Asignatura:** Cálculo Integral 
**Fecha:** 29 de enero de 2026