# 📈 Simulador de Bolsa Web con Análisis de Portafolio

Este proyecto consiste en una aplicación web interactiva diseñada para simular el comportamiento de los mercados financieros. Permite a los usuarios gestionar un portafolio virtual, aplicar estrategias de inversión y analizar el riesgo utilizando conceptos estadísticos y financieros.

## 🚀 Características Principales

* **Simulación en Tiempo Real:** Compra y venta de activos con datos financieros reales integrados mediante la API de Alpha Vantage.
* **Gestión de Portafolio:** Cálculo automático del valor total del portafolio y del Retorno de Inversión (ROI).
* **Estrategias de Trading:** Implementación de algoritmos para simular estrategias como *Buy and Hold* y *Momentum*.
* **Análisis de Riesgo:** Módulo para calcular la volatilidad de los activos basada en la desviación estándar.
* **Predicciones con IA:** Generación de estimaciones de precios futuros mediante modelos probabilísticos.

---

## 🛠️ Arquitectura y Tecnologías

El sistema está construido bajo una arquitectura de tres capas:

1.  **Frontend:** Interfaz dinámica desarrollada con **HTML5, CSS3 y JavaScript**.
2.  **API Externa:** Integración con **Alpha Vantage** para la obtención de cotizaciones reales.
3.  **Base de Datos:** Uso de **Supabase (PostgreSQL)** para el almacenamiento persistente del historial de operaciones.

### Fórmulas Implementadas
Para el análisis financiero, el simulador utiliza:
* **Valor del Portafolio:** $\sum_{i=1}^{n} \text{Cantidad}_i \times \text{Precio}_i$
* **ROI:** $\frac{\text{Valor actual} - \text{Inversión inicial}}{\text{Inversión inicial}} \times 100$
* **Volatilidad ($\sigma$):** $\sqrt{\frac{\sum (x_i - \mu)^2}{n}}$

---

## 📂 Estructura de Archivos
* `index.html`: Estructura principal de la interfaz de usuario.
* `script.js`: Lógica de negocio, consumo de APIs y cálculos financieros.
* `style.css`: Diseño y estilos visuales de la plataforma.
* `documento.pdf`: Documentación técnica detallada del proyecto.
* `documento.tex`: Código fuente en LaTeX de la documentación.

---
**Autor:** Williams Espinosa López
**Docente:** Sirgei García Ballinas
**Asignatura:** Cálculo Integral
**Fecha:** 17 de marzo de 2026