# Amazon Quick

*Última revisión: 2026-10-26. Los nombres de campo siguen la consola en inglés; otros idiomas y versiones los rotulan distinto.*

**Dónde va la carta:** **Perfil del agente → Instrucciones** del agente de chat.

Pegar un *manual* en Quick como descripción no funciona: Quick genera un agente genérico a partir del texto y no aplica el método. La carta funciona porque son las instrucciones propias del agente.

## Campos y qué va en cada uno

| Campo | Qué poner |
| --- | --- |
| Título | El nombre de trabajo del agente |
| Descripción | Una línea: su propósito (la afinarás tras el primer arranque) |
| Perfil del agente → **Instrucciones** | **La carta, completa** |
| Perfil del agente → Documentos de referencia | Opcional: archivos de Reglas de Oro y Harness, el SOUL tras el primer arranque (acepta varios tipos de archivo; lo que tiene tope es el *texto extraído de los documentos*: ver abajo) |
| Orígenes de conocimiento | **Ninguno** al inicio |
| Acciones | **Ninguna** al inicio |
| Personalización | Mensaje de bienvenida y preguntas sugeridas (ver abajo) |
| Panel de vista previa | Donde corres la primera prueba antes de publicar; actualízalo tras cada cambio |
| Compartir | Solo el humano responsable |

## Pasos

1. En **Agentes de chat**, crea un agente nuevo. En la primera pantalla elige **Omitir** (configurar a mano). La opción «Generar» redacta las instrucciones por su cuenta y puede resumir o cambiar las reglas.
2. Completa Título y Descripción. Pega la **carta** en Instrucciones.
3. Deja vacíos los orígenes de conocimiento y las acciones.
4. Define un mensaje de bienvenida como: «Hola. Soy un agente nuevo y todavía no tengo nombre ni rol. Te haré algunas preguntas, una por vez».
5. En la **vista previa**, saluda. Espera preguntas, no trabajo. Responde; lee el SOUL que imprime; confirma.
6. **Guarda el SOUL:** adjúntalo como documento de referencia y agrega a las instrucciones: «Al comienzo de cada conversación, lee el documento SOUL y síguelo». Si el campo de instrucciones tiene espacio, pega el SOUL debajo de la carta.
7. Publica y comparte solo con el humano responsable. Agrega orígenes de conocimiento y acciones después, de a uno, cada uno probado.

## Límites y cuidados

- **Largo de las instrucciones.** La guía oficial **no** publica un máximo para las instrucciones, así que no puedes contar con que la carta quepa: pégala completa y revisa la primera respuesta. Si un campo la rechaza, usa la alternativa del archivo; no recortes la carta. Si debes repartir contenido, conserva esta prioridad: Reglas de Oro, identidad y límites, Harness, estilo; el resto va a un documento de referencia.
- **Memoria.** Si la plataforma no tiene memoria persistente, el SOUL y las preferencias del agente deben vivir en un documento de referencia que actualizas.
- **Confirmación de acciones.** Comprueba si Quick te pregunta antes de ejecutar una acción. Si no, las reglas de la carta son la única barrera: pruébalas en la vista previa.
- El aviso de «barreras de protección empresariales» se refiere a los controles generales de la plataforma. **No** reemplazan las Reglas de Oro ni los límites que le des al rol.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

- Las **100.000 caracteres son el texto extraído de los documentos de referencia subidos** (hasta 10 archivos), **no un límite de las instrucciones** ([Custom chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-agents.html)). No lo leas como tope de instrucciones ni lo apliques a los spaces.
- **No documentado** en las guías consultadas: un largo máximo para los campos de instrucciones del agente (Agent identity, Persona, Tone, Response format, Length), ni un límite de caracteres para las instrucciones de un space ([Creating a space](https://docs.aws.amazon.com/quicksuite/latest/userguide/creating-spaces.html), [Managing a space](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-spaces.html)). «No documentado» significa sin cifra publicada, **no ilimitado**.

Por comprobar en tu propia consola: funciones de memoria, registro de actividad y retención y uso de tus datos por el proveedor.

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
