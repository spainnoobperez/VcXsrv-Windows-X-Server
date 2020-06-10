# VcXsrv-Windows-X-Server
Requisito previo:
- Visual Studio 2017 Edición comunitaria
- Strawberry perl edición portátil instalada en c:\perl
- Cygwin (Instale las herramientas necesarias cuando se vean errores: nasm, flex, bison, python, ....)
- Para construir el instalador: nsis

Ejecute buildall.sh 1 9 para compilar la versión de 64 bits y buildall.sh 0 9 para la versión de 32 bits.
(El segundo número en la línea de comando es el número de procesos paralelos a utilizar, lo que podría depender del número de núcleos físicos de CPU)
