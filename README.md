# **Análisis de productos en Amazon con web scraping**

---

![Amazon!](./img/amazon.png "Amazon")

---

- [Extracción de datos de la pagina web de amazon con web scraping con python](#extracción-de-datos-de-la-pagina-web-de-amazon-con-web-scraping-con-python)

  - [Nomenclatura de los datos](#nomenclatura-de-los-datos)

- [Limpiar y Filtrar los datos mas relevantes](#limpiar-y-filtrar-los-datos-mas-relevantes)

- [Estadisticas y Transformacion de los datos](#estadisticas-y-transformacion-de-los-datos)
- [Conclusión](#conclusión)

---

## **Extracción de datos de la pagina web de amazon con web scraping con python**

El Siguiente proyectos se basa extraer los datos de la pagina web se Amazon por medio de Web Scraping.

Los Datos seran los Monitores de ofrece Amazon. lo encontrará [aquí](https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011&language=es&ref=nav_em__nav_desktop_sa_intl_monitors_0_2_6_8 "Monitores").

El procedimiento para la extracción de datos para un análisis de la página web de Amazon utilizando web scraping con Beautiful Soup en Python es el siguiente:

- **Instalar Beautiful Soup:**

Primero, debe asegurarse de tener instalada la biblioteca Beautiful Soup. Puede instalarla utilizando pip en su terminal de comando, por ejemplo: pip install beautifulsoup4.

- Identificar la URL de la página web de Amazon que contiene los datos que se desean extraer.

- **Inspeccionar la página web:**

Abra la página web en su navegador y use las herramientas de desarrollador del navegador para inspeccionar los elementos HTML de la página y encontrar los elementos que contienen los datos que desea extraer.

- **Crear una solicitud HTTP:**

Utilice la biblioteca Requests para enviar una solicitud HTTP a la URL de la página web que desea extraer. Esto le permitirá obtener el contenido HTML de la página web.

- **Crear un objeto Beautiful Soup:**

Utilice Beautiful Soup para analizar el contenido HTML y crear un objeto de tipo Beautiful Soup. Esto le permitirá extraer datos específicos del contenido HTML.

- **Extraer datos específicos:**

Utilice las funciones de Beautiful Soup para extraer datos específicos de los elementos HTML que identificó previamente en la página web. Por ejemplo, puede usar la función find o find_all para buscar elementos HTML específicos por su etiqueta, clase o atributo.

- **Almacenar los datos extraídos:**

Almacene los datos extraídos en una estructura de datos adecuada, como un diccionario o una lista, para su posterior análisis.

- **Procesar los datos extraídos:**

Limpie y procese los datos extraídos según sea necesario, como convertir los precios en números, eliminar caracteres no deseados, etc.

- **Automatizar el proceso:**

Utilice bucles y la función de paginación para automatizar el proceso de extracción de datos y recopilar datos de varias páginas web en Amazon.

---

![Web Scraping!](./img/Web-scraping.png "Web Scraping")

---

### **Nomenclatura de los datos**

Para hacer gráficos estadísticos para un análisis de la página web de Amazon utilizando web scraping con Python, se necesitarán extraer datos relevantes de la página web. Algunos de los datos que pueden ser relevantes para el análisis incluyen:

- **Productos:**

  Nombre del producto.

- **Precio_Nuevo:**

  Precio Despues de aplicarle el descuento.

- **Precio_Antes:**

  Precio sin aplicarle el descuento.

- **Stock:**

  Cantidad de Unidades almacenada.

- **Ranking:**

  Apreciacion de los productos el rango es [0-5]

- **Votantes:**

  Cantidad de persona que dieron su apreciacion a los productos.

- **Porcentaje_Ranking**

  Se calcula: [(Ranking_Maximo - Ranking) / Ranking_Maximo] \* 100%

  Ranking_Maximo = 5

- **Descuentos**

  Se calcula: [(Precio_Antes - Precio_Nuevo) / Precio_Antes] \* 100%

[🔼](#análisis-de-productos-en-amazon-con-web-scraping)

---

## **Limpiar y Filtrar los datos mas relevantes**

- **Eliminar valores duplicados:**

Los datos duplicados pueden introducir errores en el análisis y deben eliminarse.

- **Revisar valores faltantes:**

Si hay valores faltantes, debe determinarse si es posible imputarlos o si deben eliminarse las filas correspondientes.

- **Verificar la consistencia de los datos:**

Los valores extremos o inesperados pueden ser señal de errores en la recolección de datos y deben verificarse y, si es necesario, corregirse.

- **Verificar la calidad de los datos:**

Los datos incompletos, inconsistentes o incorrectos pueden ser una señal de problemas en la calidad de los datos y deben ser corregidos.

- **Normalizar los datos:**

Los valores de los datos pueden estar en diferentes escalas o unidades, lo que puede dificultar la comparación entre ellos. Es posible que deba normalizar los datos para facilitar el análisis.

- **Verificar la precisión de los datos:**

los errores de entrada de datos pueden introducir errores en el análisis. Por lo tanto, debe verificar que los datos se ingresaron correctamente y hacer correcciones si es necesario.

- **Estandarizar los datos:**

Los nombres de columnas o variables pueden variar en diferentes conjuntos de datos. Para facilitar el análisis, es posible que deba estandarizar los nombres de las variables.

[🔼](#análisis-de-productos-en-amazon-con-web-scraping)

---

## **Estadisticas y Transformacion de los datos**

- **Histograma de precios:**

Puedes crear un histograma que muestre la distribución de precios de tus productos. Esto puede ayudarte a identificar el rango de precios más común y a entender cómo se comparan tus productos en términos de precio.

- **Gráfica de barras de descuentos:**

Puedes crear una gráfica de barras que muestre la cantidad de productos que tienen diferentes niveles de descuento. Esto puede ayudarte a entender cómo los descuentos afectan las ventas de tus productos y a identificar qué productos tienen los mayores descuentos.

- **Gráfica de dispersión de ranking y votos:**

Puedes crear una gráfica de dispersión que muestre el ranking de tus productos en Amazon en función del número de votantes. Esto puede ayudarte a entender la relación entre la popularidad de tus productos y su ranking en Amazon.

- **Gráfica de líneas de stock:**

Puedes crear una gráfica de líneas que muestre cómo cambia el stock de tus productos con el Descuentos. Esto puede ayudarte a planificar mejor tus inventarios y a evitar quedarte sin stock de tus productos.

- **Gráfica de barras de porcentaje de ranking:**

Puedes crear una gráfica de barras que muestre el porcentaje de productos que tienen diferentes rangos de ranking. Esto puede ayudarte a entender cómo se comparan tus productos en términos de ranking y a identificar los productos que tienen los mejores y peores rangos de ranking.

- **Palabras Clave**

[🔼](#análisis-de-productos-en-amazon-con-web-scraping)

---

## **Conclusión**

- **Histograma de precios:**

* La gráfica muestra la distribución de precios de productos en Amazon, comparando el precio nuevo y el precio antes de una modificación.

* Podemos ver que la mayoría de los precios nuevos se encuentran entre los $20 y $40, mientras que la mayoría de los precios anteriores se encuentran entre los $40 y $60. Además, podemos notar que hay una mayor cantidad de productos con precios anteriores más altos que de productos con precios nuevos más altos.

* La gráfica también muestra que algunos productos tuvieron una disminución significativa en el precio después de la modificación, mientras que otros tuvieron un aumento en el precio. En general, parece haber una tendencia a la baja en los precios después de la modificación.

En conclusión, esta gráfica nos permite visualizar la distribución de precios de productos en Amazon y comparar los precios antes y después de una modificación. Además, podemos observar tendencias en los cambios de precios después de la modificación.

- **Gráfica de barras de descuentos:**

* La gráfica muestra la cantidad de productos en cada intervalo de descuento.

* Podemos observar que la mayoría de los productos tienen descuentos menores del 20%, mientras que un porcentaje menor de productos tienen descuentos más altos, con una cantidad cada vez menor de productos a medida que aumenta el porcentaje de descuento.

* La gráfica también nos permite comparar visualmente la cantidad de productos en cada intervalo de descuento. Podemos ver que la cantidad de productos disminuye significativamente a medida que aumenta el porcentaje de descuento.

En conclusión, esta gráfica nos permite visualizar la distribución de descuentos en los productos de Amazon y ver la cantidad de productos en cada intervalo de descuento. Esto puede ser útil para comprender mejor las estrategias de precios de Amazon y cómo los consumidores pueden aprovechar los descuentos.

- **Gráfica de dispersión de ranking y votos:**

* La gráfica de dispersión muestra la relación entre el número de votantes y el ranking de los productos en Amazon.

* Podemos observar que no hay una correlación clara entre el número de votantes y el ranking de los productos. Hay productos con muchos votantes que tienen un ranking bajo y otros con pocos votantes que tienen un ranking alto.

* Esto puede indicar que otros factores, como la calidad del producto, la marca o el precio, pueden influir en el ranking de los productos en Amazon, además del número de votantes.

En conclusión, esta gráfica nos muestra que no hay una relación directa entre el número de votantes y el ranking de los productos en Amazon, lo que sugiere que otros factores pueden ser importantes en la clasificación de los productos.

- **Gráfica de líneas de stock:**

* En esta gráfica se puede observar la relación entre el descuento y el stock de los productos. Se han representado dos líneas, una para el top 20 de productos con mayor descuento y otra para el top 10 de productos con mayor descuento.

* Podemos observar que los productos con mayor descuento suelen tener menor stock disponible, lo cual es lógico ya que es probable que haya una mayor demanda de estos productos y por tanto se vendan más rápidamente. Además, podemos observar que la relación entre descuento y stock no es lineal, ya que el stock parece disminuir de forma más pronunciada en los productos con mayores descuentos.

- **Gráfica de barras de porcentaje de ranking:**

La gráfica muestra la distribución de la cantidad de productos que tienen un determinado porcentaje de ranking en Amazon. Se observa que la mayoría de los productos se encuentran en un rango de porcentaje de ranking entre 0% y 5%, y que a medida que el porcentaje de ranking aumenta, la cantidad de productos disminuye. Esto sugiere que es más difícil para los productos obtener un alto porcentaje de ranking en Amazon y que hay una gran cantidad de productos con bajos porcentajes de ranking.

- **Palabras Claves:**

Este código nos permite analizar las palabras más comunes en la descripción de los productos en el dataset. A partir de las 10 palabras más comunes, se podrían inferir posibles categorías de productos que se encuentran en el dataset. Además, si se quisiera profundizar en el análisis, se podría hacer un análisis de sentimiento de las descripciones de los productos para entender mejor cómo se presentan los productos en el mercado.

[🔼](#análisis-de-productos-en-amazon-con-web-scraping)

---
