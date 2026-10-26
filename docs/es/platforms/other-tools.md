# Otras herramientas

*Última revisión: 2026-10-26. Los nombres cambian rápido; esta página enseña qué buscar.*

Toda herramienta tiene alguna forma de **texto que vale para todas las conversaciones**. Usa estos ejemplos como guía y confirma los nombres en la documentación del producto.

| Familia | Dónde suele ir la carta | El SOUL |
| --- | --- | --- |
| Asistentes de IDE (Cursor, Windsurf, GitHub Copilot…) | Un archivo de reglas/instrucciones del espacio de trabajo (p. ej. `AGENTS.md`, o la carpeta de reglas propia de la herramienta) | El agente puede escribir `SOUL.md` en el espacio de trabajo si las herramientas de archivos están activas. Usa un espacio vacío. |
| Constructores de asistentes (Copilot Studio, agentes de Le Chat, Perplexity Spaces…) | Las *Instrucciones* / instrucciones personalizadas del asistente | Lo guardas tú en las instrucciones o en un archivo de conocimiento |
| API o SDK (escribes el programa) | El **prompt de sistema** de tu solicitud | Tu código lo guarda; cárgalo al prompt de sistema en cada inicio |
| Cualquier cosa con solo un cuadro de chat | El **primer mensaje** de una conversación nueva | Pégalo de nuevo al empezar cada conversación |

## Lista de comprobación para cualquier herramienta

1. ¿Hay un campo que valga para *toda* conversación con este agente? Pon ahí la carta.
2. Si el campo es muy corto, usa un aviso corto más una copia adjunta de la carta, y verifica en la primera respuesta que el agente sigue el protocolo hasta el final.
3. ¿El agente puede escribir archivos? Si sí, dale una carpeta vacía dedicada. Si no, planifica guardar el SOUL tú mismo.
4. ¿Qué herramientas, conectores o acciones están activos? Apágalos hasta que el SOUL declare una necesidad.
5. ¿La herramienta registra la actividad? ¿Dónde?
6. ¿Quién más puede abrir el agente? Mantenlo privado.

Mira las [ocho preguntas](README.md#ocho-preguntas-antes-de-elegir-o-configurar-una-plataforma) para el resto.
