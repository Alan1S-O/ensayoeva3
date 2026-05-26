# ensayoeva3
Ensayo para evaluacion de programacion
Aquí tienes una propuesta completa y bien estructurada para el `README.md` de tu repositorio en GitHub. He incluido las secciones estándar que hacen que un proyecto se vea profesional y fácil de entender.

---

# ✈️ Registro de Equipaje - VueloCHILE

Este es un programa interactivo desarrollado en **Python** para la gestión, validación y clasificación automatizada del equipaje de los pasajeros de la aerolínea **VueloCHILE**.

El script recopila de forma segura los datos de cada bulto, valida que cumplan con las políticas de la empresa y genera un manifiesto de carga final dividiendo el equipaje según su peso.

---

## 🚀 Características principales

* **Validaciones robustas:**
* Controla que la cantidad de equipajes y sus pesos sean valores numéricos enteros positivos (evitando caídas del sistema mediante `try-except`).
* Restringe el código del ticket para que tenga una longitud mínima de 5 caracteres y no contenga espacios intermedios.


* **Clasificación automatizada:**
* **Equipaje de Cabina:** Pesos menores o iguales a 10 kg.
* **Equipaje de Bodega:** Pesos superiores a 10 kg.


* **Manifiesto de carga:** Al finalizar los registros, muestra un resumen claro con el total de bultos asignados a cada sección del avión.

---

## 🛠️ Requisitos

* **Python 3.x** instalado en tu sistema.

---

## 📦 Instalación y Uso

1. **Clona este repositorio** en tu máquina local:
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git

```



```
2. **Navega al directorio** del proyecto:
   ```bash
   cd TU_REPOSITORIO

```

3. **Ejecuta el script**:
```bash
python registro_equipaje.py

```



```

---

## 📋 Ejemplo de ejecución

```text
=== Registro de de equipaje -VueloCHILE ===
cuantos equipajes desea registrar: 2

-- Registro del equipaje 1 ---
ingrese codigo de tiquet (min 5 caracteres, sin espacio): VCH123
ingrese el peso del equipaje en kg (entero positivo): 8
clasificado como equipaje cabina

-- Registro del equipaje 2 ---
ingrese codigo de tiquet (min 5 caracteres, sin espacio): VCH456
ingrese el peso del equipaje en kg (entero positivo): 23
clasificado como equipaje de bodega

===========================================================
¡El avión transportará 1 equipajes en Cabina y 1 equipajes en Bodega! ¡Manifiesto de carga listo!
===========================================================

```

---

## 🛠️ Tecnologías utilizadas

* **Lenguaje:** Python 3
* **Conceptos aplicados:** Ciclos (`while`, `for`), manejo de excepciones (`try-except`), condicionales y manipulación de strings.

---

> 📌 **Nota de optimización para el desarrollador:**
> Dentro de tu código actual, tienes dos pequeños detalles técnicos que podrías pulir:
> 1. En la línea `f"\n-- Registro del equipaje 0° {i+i} ---"`, si deseas mostrar el número correlativo correcto (1, 2, 3...), te conviene cambiarlo por `{i + 1}`.
> 2. En el bucle de validación de peso, el mensaje de *"Error de pesaje"* se imprime siempre (incluso si el peso es correcto) debido a que no está dentro del bloque `except` o un condicional `if`. ¡Moverlo dentro del `except` resolverá el comportamiento!
> 
>
