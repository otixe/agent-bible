# Si algo sale mal

| Síntoma | Causa probable | Qué hacer |
| --- | --- | --- |
| Responde con **trabajo** en vez de preguntas | La carta no se cargó (muy larga, campo equivocado, un archivo superior la pisa) o el modelo se saltó el protocolo | Comprueba que pegaste en el campo que vale para toda conversación; mira la [página de tu plataforma](platforms/README.md) por límites de tamaño; si hace falta pega la carta como primer mensaje y pide: «Ejecuta tu protocolo de primer arranque antes que nada». |
| **Inventa una personalidad** o un nombre | Llenó los vacíos en vez de preguntar | Di: «No tienes nombre ni rol todavía. Pregúntame». Si persiste, la carta no se está cargando completa. |
| Empieza a **crear agentes** | El modelo leyó un texto tipo manual como su trabajo | Quizás pegaste algo distinto de la carta. La carta dice explícitamente que el agente no es creador. Pega solo la carta en una conversación nueva. |
| Pide **contraseñas o claves** | Rompe la regla de secretos | Nunca se las des. Agrega la falla a tus pruebas; corrige el SOUL; vuelve a probar. |
| Dice tener **herramientas que no tiene** | Está adivinando | Pídele que liste exactamente lo que puede hacer; compáralo con tu configuración; corrige la respuesta a la pregunta 4. |
| **Olvida quién es** en la siguiente conversación | El SOUL no se guardó donde la plataforma lo recarga | Sigue la sección «Dónde vive el SOUL» de la [página de tu plataforma](platforms/README.md). |
| **Actúa sin confirmación** | La plataforma lo permite y no se siguió la regla | Trátalo como una prueba de límite fallida: primero ajusta permisos (solo lectura), luego corrige el SOUL y vuelve a probar antes de usarlo. |
| La carta **no cabe** en el campo | Límite de largo de la plataforma | Usa la alternativa de aviso más archivo en la página de tu plataforma y verifica en la primera respuesta. |
| **Modelos distintos se comportan distinto** | Los modelos siguen instrucciones largas con distinta fidelidad | Repite la revisión del primer arranque y las pruebas de reglas con el modelo que realmente usas. |

## Si nada funciona

Empieza una conversación nueva con **solo** la carta, nada más en el contexto, y compara. Muchos problemas vienen de otras instrucciones o archivos que rodean la carta.

¿Encontraste un hueco en estas páginas o en las cartas? Abre un issue describiendo la plataforma, el modelo y lo que viste.
