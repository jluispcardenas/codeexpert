-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: algo
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `challenges_challenge`
--

LOCK TABLES `challenges_challenge` WRITE;
/*!40000 ALTER TABLE `challenges_challenge` DISABLE KEYS */;
INSERT INTO `challenges_challenge` VALUES (1,'Add Digits','Dado un número entero no negativo, agregue repetidamente todos sus dígitos hasta que el resultado tenga solo un dígito.\r\n\r\n<b>Ejemplo:</b>\r\n<code>\r\nInput: 38\r\nOutput: 2\r\n \r\nExplicación: El proceso es como: 3 + 8 = 11, 1 + 1 = 2.\r\n\r\nComo 2 tiene solo un dígito, devuélvalo.\r\n</code>\r\n\r\n<b> Seguimiento: </b>\r\n¿Podría hacerlo sin ningún bucle o recursión en el tiempo de ejecución O (1)?','add-digits','class Solution:\r\n    def addDigits(self, num: int) -> int:',11,3,1,'2020-05-31 00:13:43.459990','2020-06-03 14:58:49.748577',1,'easy'),(2,'Spiral Matrix','Dada una matriz de m x n elementos (m filas, n columnas), devuelve todos los elementos de la matriz en orden espiral.\r\n\r\n<b>Ejemplo 1</b>:\r\n<code>\r\nEntrada:\r\n[\r\n  [1, 2, 3],\r\n  [4, 5, 6],\r\n  [7, 8, 9]\r\n]\r\nSalida: [1,2,3,6,9,8,7,4,5]\r\n</code>\r\n\r\n\r\n<b>Ejemplo 2</b>\r\n\r\n<code>\r\nEntrada:\r\n[\r\n   [1, 2, 3, 4],\r\n   [5, 6, 7, 8],\r\n   [9,10,11,12]\r\n]\r\n\r\nSalida: [1,2,3,4,8,12,11,10,9,5,6,7]\r\n</code>','spiral-matrix','class Solution:\r\n    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:',2,0,1,'2020-06-01 16:36:32.342584','2020-06-04 00:20:47.024545',1,'medium'),(3,'Defanging an ip address','Dada una dirección IP válida (IPv4), devuelve una versión defanged de esa dirección IP.\r\n\r\nUna dirección IP defanged reemplaza cada punto \".\" con \"[.]\".\r\n\r\n<b>Ejemplo 1:</b>\r\n <code>\r\nInput: address = \"1.1.1.1\"\r\nOutput: \"1[.]1[.]1[.]1\"\r\nExample 2:\r\n</code>\r\n\r\n<b>Ejemplo 2</b>\r\n<code>\r\nInput: address = \"255.100.50.0\"\r\nOutput: \"255[.]100[.]50[.]0\"\r\n</code>\r\n\r\n<b>Restricciones:</b>\r\n\r\nLa dirección dada es una dirección IPv4 válida.','defanging-an-ip-address','class Solution:\r\n    def defangIPaddr(self, address: str) -> str:',9,1,1,'2020-06-01 16:54:23.714723','2020-06-04 00:33:31.704682',1,'easy'),(4,'Excel Sheet Column Number','Dado un título de columna como aparece en una hoja de Excel, devuelva su número de columna correspondiente.\r\n\r\n<b>Por ejemplo:</b>\r\n<code>\r\n     A -> 1\r\n     B -> 2\r\n     C -> 3\r\n     ...\r\n     Z -> 26\r\n     AA -> 27\r\n     AB -> 28\r\n     ...\r\n</code>\r\n\r\n<b>Ejemplo 1:</b>\r\n\r\n<code>\r\nEntrada: \"A\"\r\nSalida: 1\r\n</code>\r\n\r\n<b>Ejemplo 2\r\n\r\n<code>\r\nEntrada: \"AB\"\r\nSalida: 28\r\n</code>\r\n\r\n<b>Ejemplo 3</b>\r\n<code>\r\nEntrada: \"ZY\"\r\nSalida: 701\r\n</code>','excel-sheet-column-number','class Solution:\r\n    def titleToNumber(self, s: str) -> int:',0,0,1,'2020-06-01 17:04:49.424350','2020-06-01 17:04:49.424396',1,'easy'),(5,'Majority Element','Dada una matriz de tamanio <i>n</i>, encuentre el elemento mayoritario. El elemento mayoritario es el elemento que aparece mas de n / 2  veces.\r\n\r\nPuede suponer que la matriz no está vacía y que el elemento mayoritario siempre existe en la matriz.\r\n\r\n<b>Ejemplo 1:</b>\r\n<code>\r\nEntrada: [3,2,3]\r\nSalida: 3\r\n</code>\r\n\r\n<b>Ejemplo 2</b>\r\n<code>\r\nEntrada: [2,2,1,1,1,2,2]\r\nSalida: 2\r\n</code>','majority-element','class Solution:\r\n    def majorityElement(self, nums: List[int]) -> int:',0,0,1,'2020-06-01 17:25:53.846201','2020-06-01 17:33:29.953058',1,'easy'),(6,'Find the Duplicate Number','Dado un conjunto de números que contienen n + 1 enteros donde cada entero está entre 1 yn (inclusive), demuestre que debe existir al menos un número duplicado. Suponga que solo hay un número duplicado, encuentre el número duplicado.\r\n\r\n<b>Ejemplo 1:</b>\r\n\r\n<code>\r\nEntrada: [1,3,4,2,2]\r\nSalida: 2\r\n</code>\r\n\r\n<b>Ejemplo 2</b>\r\n\r\n<code>\r\nEntrada: [3,1,3,4,2]\r\nSalida: 3\r\n</code>\r\n\r\n<b>Nota:</b<\r\n\r\n1 No debe modificar la matriz (suponga que la matriz es de <b>solo lectura</b>).\r\n2 Debe usar solo un espacio adicional constante, O (1).\r\n3 Su complejidad de tiempo de ejecución debe ser menor que O (n2).\r\n4 Solo hay un número duplicado en la matriz, pero podría repetirse más de una vez.','find-the-duplicate-number','class Solution:\r\n    def findDuplicate(self, nums: List[int]) -> int:',0,0,1,'2020-06-01 17:37:53.552464','2020-06-01 17:37:53.552505',1,'medium'),(7,'Pascals Triangle','Dado un número entero no negativo de filas, genera las primeras filas del triángulo de Pascal.\r\n\r\n\r\nEn el triángulo de Pascal, cada número es la suma de los dos números directamente encima de él.\r\n\r\n<p>Ejemplo:</p>\r\n<code>\r\nEntrada: 5\r\nSalida:\r\n[\r\n      [1]\r\n     [1,1]\r\n    [1,2,1]\r\n   [1,3,3,1]\r\n  [1,4,6,4,1]\r\n]\r\n</code>','pascals-triangle','class Solution:\r\n    def generate(self, numRows: int) -> List[List[int]]:',0,0,1,'2020-06-01 17:43:54.363804','2020-06-01 17:43:54.363846',1,'easy'),(8,'Happy Number','Escriba un algoritmo para determinar si un número n es \"feliz\".\r\n\r\nUn número feliz es un número definido por el siguiente proceso: comenzando con cualquier número entero positivo, reemplace el número por la suma de los cuadrados de sus dígitos y repita el proceso hasta que el número sea igual a 1 (donde permanecerá), o se repite. sin fin en un ciclo que no incluye 1. Los números para los que este proceso termina en 1 son números felices.\r\n\r\nDevuelve True si n es un número feliz y False si no.\r\n\r\n<b>Ejemplo:</b>\r\n<code>\r\nEntrada: 19\r\nSalida: verdadero\r\n\r\nExplicación:\r\n12 + 92 = 82\r\n82 + 22 = 68\r\n62 + 82 = 100\r\n12 + 02 + 02 = 1\r\n</code>','happy-number','class Solution:\r\n    def isHappy(self, n: int) -> bool:',0,0,1,'2020-06-01 17:45:08.048951','2020-06-01 17:45:08.049019',1,'easy'),(9,'Valid parentheses','Dada una cadena que contiene solo los caracteres \'(\', \')\', \'{\', \'}\', \'[\' y \']\', determine si la cadena de entrada es válida.\r\n\r\nUna cadena de entrada es válida si:\r\n\r\nLos corchetes abiertos deben cerrarse con el mismo tipo de corchetes.\r\nLos corchetes abiertos deben cerrarse en el orden correcto.\r\nTenga en cuenta que una cadena vacía también se considera válida.\r\n\r\n<b>Ejemplo 1:</b>\r\n\r\n<code>\r\nEntrada: \"()\"\r\nSalida: verdadero\r\nEjemplo 2\r\n\r\nEntrada: \"() [] {}\"\r\nSalida: verdadero\r\nEjemplo 3\r\n\r\nEntrada: \"(]\"\r\nSalida: falso\r\nEjemplo 4\r\n\r\nEntrada: \"([)]\"\r\nSalida: falso\r\nEjemplo 5:\r\n\r\nEntrada: \"{[]}\"\r\nSalida: verdadero\r\n\r\n</code>','valid-parentheses','class Solution:\r\n    def isValid(self, s: str) -> bool:',0,0,1,'2020-06-01 17:52:41.608312','2020-06-01 17:52:41.608379',1,'easy'),(10,'Factorial Trailing Zeroes','Dado un número entero n, devuelve el número de ceros finales en n !.\r\n\r\n<b>Ejemplo 1:</b>\r\n<code>\r\nEntrada: 3\r\nSalida: 0\r\nExplicación: 3! = 6, sin cero al final.\r\n</code>\r\n\r\n<b>Ejemplo 2</b>\r\n\r\n<code>\r\nEntrada: 5\r\nSalida: 1\r\nExplicación: 5! = 120, un cero al final.\r\n</code>\r\n\r\n<b>Nota</b>: Su solución debe estar en complejidad de tiempo logarítmico.','factorial-trailing-zeroes','class Solution:\r\n    def trailingZeroes(self, n: int) -> int:',0,0,1,'2020-06-01 17:59:38.594288','2020-06-01 18:04:05.211600',1,'easy');
/*!40000 ALTER TABLE `challenges_challenge` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-03 21:16:25