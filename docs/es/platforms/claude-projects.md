# Claude Projects

*Última revisión: 2026-10-26.*

**Dónde va la carta:** las **Instrucciones** del proyecto. Valen para toda conversación dentro del proyecto, que es justo lo que quieres.

## Pasos

1. En Claude, crea un **proyecto nuevo** con el nombre de trabajo del agente (lo renombrarás tras el primer arranque).
2. Abre las instrucciones del proyecto y **pega la carta completa**.
3. Opcional: sube las [Reglas de Oro](../../../reglas/es/REGLAS-DE-ORO.md) y el [Harness](../../../harness/es/HARNESS-AGENTE-SOLO.md) como archivos del proyecto, para poder señalarlos después. La carta ya los contiene.
4. Inicia una conversación en el proyecto y saluda. Espera preguntas, no trabajo (ver [Primer arranque](../reading-your-agent/first-run.md)).
5. Responde, lee el SOUL que imprime, corrígelo y confirma.
6. **Guarda el SOUL:** agrégalo a las instrucciones del proyecto *debajo de la carta* (o súbelo como archivo del proyecto llamado `SOUL.md` y escribe en las instrucciones que lo lea primero). Luego renombra el proyecto.

## Dónde vive el SOUL

En el proyecto: instrucciones o un archivo del proyecto. El agente no puede escribirlo por ti. Cada vez que el SOUL cambie, actualizas esa copia.

## Límites y cuidados

- Las instrucciones y los archivos del proyecto comparten la ventana de contexto del modelo con la conversación. Una carta muy larga más muchos archivos deja menos espacio para el trabajo.
- Los proyectos sirven para trabajo repetido con contexto compartido; el agente **no tiene herramientas** que tú no conectaste. Mantén los conectores apagados hasta que el SOUL declare una necesidad.
- Las funciones de memoria de la plataforma (si están activas) son aparte del SOUL y la carta no las controla. Revisa qué se recuerda y borra lo que no deba estar.
- Compartir un proyecto comparte sus instrucciones. Mantenlo privado para el humano responsable.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

- **Disponibilidad:** los Projects tradicionales están disponibles para todos los usuarios, Free incluido (Free: máximo 5 proyectos); compartir con Team/Enterprise depende de la configuración del administrador ([crear y gestionar proyectos](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), [personalización](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features), [¿qué son los proyectos?](https://support.claude.com/en/articles/9517075-what-are-projects)).
- **Una versión nueva de Projects (beta)** se despliega de forma selectiva a Pro/Max, primero a usuarios de Claude Code y algunas migraciones de proyectos existentes; la guía dice que otros planes y superficies siguen después. No supongas que la tienes: esta página describe los Projects tradicionales ([¿qué son los proyectos?](https://support.claude.com/en/articles/9517075-what-are-projects)).

## No documentado — compruébalo tú

- **Un largo máximo para las instrucciones del proyecto** no está publicado en las páginas oficiales consultadas. No tomes prestados los límites de `CLAUDE.md` de Claude Code ni leas la ventana de contexto o la recuperación como un tope de instrucciones. Pega la carta y, en la primera respuesta, confirma que el agente realmente empieza con las preguntas.

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
