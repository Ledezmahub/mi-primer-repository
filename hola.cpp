// ============================================================
// ARCHIVO: hola.cpp
// Descripción: Programa básico en C++ con explicaciones paso a paso
// ============================================================

// PASO 1: INCLUSIONES DE LIBRERÍAS
// La directiva #include permite usar funciones predefinidas
// <iostream> es la librería estándar para entrada/salida (Input/Output)
#include <iostream>

// PASO 2: USAR EL ESPACIO DE NOMBRES ESTÁNDAR
// 'using namespace std;' permite usar funciones como cout sin escribir 'std::cout'
// Nota: En proyectos grandes, es mejor evitar esto y usar 'std::' explícitamente
using namespace std;

// PASO 3: FUNCIÓN PRINCIPAL
// 'int main()' es el punto de entrada de todo programa C++
// 'int' significa que la función retorna un número entero
// '()' indica que la función no recibe parámetros (argumentos)
int main()
{
    // PASO 4: MOSTRAR TEXTO EN LA PANTALLA
    // 'cout' es el comando para imprimir en consola
    // '<<' es el operador de inserción (envía datos al flujo de salida)
    // 'endl' inserta una nueva línea y vacía el búfer
    cout << "¡Hola, Mundo!" << endl;
    
    // PASO 5: VARIABLES - ALMACENAR DATOS
    // Una variable es un espacio en memoria que guarda un valor
    
    // Declarar una variable de tipo 'int' (número entero)
    int edad = 25;
    
    // Declarar una variable de tipo 'double' (número con decimales)
    double altura = 1.75;
    
    // Declarar una variable de tipo 'string' (texto)
    // Nota: requiere #include <string> en proyectos reales
    string nombre = "Juan";
    
    // PASO 6: MOSTRAR VALORES DE VARIABLES
    cout << "Mi nombre es: " << nombre << endl;
    cout << "Mi edad es: " << edad << " años" << endl;
    cout << "Mi altura es: " << altura << " metros" << endl;
    
    // PASO 7: OPERACIONES MATEMÁTICAS
    int numero1 = 10;
    int numero2 = 5;
    
    int suma = numero1 + numero2;
    int resta = numero1 - numero2;
    int multiplicacion = numero1 * numero2;
    int division = numero1 / numero2;
    
    cout << "\n--- OPERACIONES MATEMÁTICAS ---" << endl;
    cout << numero1 << " + " << numero2 << " = " << suma << endl;
    cout << numero1 << " - " << numero2 << " = " << resta << endl;
    cout << numero1 << " * " << numero2 << " = " << multiplicacion << endl;
    cout << numero1 << " / " << numero2 << " = " << division << endl;
    
    // PASO 8: SENTENCIA CONDICIONAL (IF-ELSE)
    // Ejecuta código diferente según una condición
    if (edad >= 18)
    {
        cout << "\nSoy mayor de edad" << endl;
    }
    else
    {
        cout << "\nSoy menor de edad" << endl;
    }
    
    // PASO 9: BUCLE FOR
    // Repite un bloque de código una cantidad específica de veces
    cout << "\n--- CONTANDO DEL 1 AL 5 ---" << endl;
    for (int i = 1; i <= 5; i++)
    {
        cout << "Número: " << i << endl;
    }
    
    // PASO 10: RETURN
    // Finaliza el programa y retorna 0 (indica que todo fue exitoso)
    // 0 = ejecución correcta, otros valores = error
    return 0;
}

// ============================================================
// RESUMEN DE CONCEPTOS:
// 
// - #include: Incluye librerías externas
// - using namespace std: Usa el espacio de nombres estándar
// - main(): Función principal donde comienza el programa
// - cout: Imprime texto en la consola
// - endl: Salto de línea
// - Variables: Almacenan datos (int, double, string)
// - Operadores: +, -, *, /, etc.
// - if-else: Tomas decisiones en el código
// - for: Repite código varias veces
// - return 0: Finaliza el programa exitosamente
//
// ============================================================