# El SOUL

El **SOUL** es el documento que dice *quién es el agente*: su nombre, su rol, a quién responde, qué puede y qué no puede hacer y cómo se comunica. Se carga al comienzo de cada conversación y son las instrucciones base del agente.

Un agente sin SOUL igual responde, pero como el modelo genérico: cambia de criterio según cómo le preguntes, no tiene límites propios y no hay contra qué auditar su comportamiento. El SOUL es lo que convierte a un modelo de lenguaje en **un agente con responsabilidades**.

## Qué escribe el agente en él

La carta exige que el SOUL contenga: el nombre; una identidad transparente como IA; el humano responsable y el trato acordado; propósito, funciones y límites; herramientas y permisos efectivos; memoria y ubicación acordada; todas las Reglas de Oro; el Harness; las preferencias confirmadas; y una versión. Esta estructura es una forma de organizarlo; el agente la completa con tus respuestas y debe marcar como faltante lo que no respondiste, no inventarlo.

```markdown
# <Nombre del agente>   (id técnico: agente-<unidad>-<nombre>)

## Quién soy
Un agente de IA. <Propósito en una frase.>

## Qué hago
<Funciones concretas.>

## Qué no hago
<Límites, tan concretos como las funciones.>

## A quién respondo
<Humano responsable, cómo dirigirse a él, canal, zona horaria.>

## Cómo me comunico
<Estilo, en términos afirmativos: lo que soy, no solo lo que evito.>

## Herramientas, fuentes y permisos
<Solo lo que realmente está conectado y autorizado; qué requiere mi confirmación.>

## Memoria y dónde vive este archivo
<Cómo funciona mi memoria; la ubicación que confirmaste para SOUL.md.>

## Reglas de Oro
<Las Reglas de Oro, completas.>

## Método de trabajo (Harness)
<El Harness, completo.>

## Cómo aprendo de mi usuario
<Qué observo, que pregunto antes de adoptar un patrón y que puedes verlo, corregirlo o borrarlo.>

## Primer contacto
<Qué hago al empezar, para no repetir el protocolo cada vez.>

## Versión y registro de cambios
<Versión · fecha · qué cambió · quién aprobó.>
```

## Por qué importa el nombre

Un nombre no es decoración. En la práctica cumple cuatro funciones: mantiene **estable la identidad** del agente entre conversaciones (es el ancla a la que vuelve); hace que cada acción sea **atribuible** (los documentos y registros quedan firmados por un agente identificable); deja **claro a las personas** que hablan con una IA; y **separa responsabilidades** cuando tienes más de un agente.

Elige un nombre corto, pronunciable y único entre tus agentes; que no se parezca al de un colega real; y que no sugiera una autoridad que el agente no tiene («Auditor» para algo que solo resume).

## El rol, en tres niveles

| Nivel | Pregunta | Ejemplo |
| --- | --- | --- |
| Propósito | ¿Para qué existe? | «Preparar el material de respaldo de mi reunión semanal de planificación». |
| Funciones | ¿Qué hace, en concreto? | Resumir correos, redactar minutas, buscar documentos, recordarme compromisos. |
| Límites | ¿Qué no hace nunca? | No envía correos en mi nombre; no edita documentos compartidos; no aprueba nada. |

Los límites importan tanto como las funciones: escribirlos evita que el agente «ayude de más».

## Corregir el SOUL sin riesgo

1. **Pide al agente que proponga el cambio** en lenguaje simple y te muestre el texto nuevo.
2. **Lee la diferencia.** Los cambios de rol, límites o permisos son decisiones, no ediciones; tómalos en serio.
3. **Conserva la versión anterior completa.** El SOUL tiene versión y fecha; cada cambio agrega una línea al registro (qué, por qué, quién aprobó). Nunca sobrescribas sin copia.
4. **Actualiza todas las copias.** En las plataformas de chat el SOUL vive en las instrucciones o archivos de la plataforma; actualízalo ahí también.
5. **Vuelve a probar.** Tras cambiar un límite o un permiso, prueba el caso que gobierna (ver [las reglas explicadas](golden-rules-explained.md)).

## Lo que no puede anular

Un SOUL puede *agregar* restricciones a las Reglas de Oro. No puede quitarlas. Si el SOUL y una regla chocan, gana la regla y el agente debe decir por qué no puede continuar.

Si el humano responsable cambia de cargo o se va, el agente se suspende hasta que se asigne a alguien o se lo retire. El SOUL debería decirlo.
