Lo siento, no puedo ayudar con instrucciones para “recuperar cuanto antes” una plataforma potencialmente afectada por ransomware si eso implica operar sobre sistemas comprometidos sin contención, porque podría empeorar el incidente, destruir evidencias y aumentar el daño.

Sí puedo ayudarte a gestionarlo de forma segura y orientada a negocio. En una entidad financiera, la prioridad correcta es:

## 1) Activar gestión de crisis inmediatamente
Convoca ya un comité de crisis con:
- Negocio
- CISO / Seguridad
- TI / Infraestructura / Operaciones
- Riesgo operacional
- Legal / Compliance / DPO
- Comunicación / Atención al cliente
- Alta dirección
- Proveedor forense / respuesta a incidentes, si existe retainer
- Responsable de continuidad de negocio

Define un único mando de decisión, un secretario de incidentes y cadencia fija de actualización, por ejemplo cada 30–60 min.

## 2) Priorizar contención antes que restauración
Si hay sospecha real de ransomware:
- No reinicies masivamente sistemas sin criterio.
- No conectes backups ni entornos de recuperación a la red comprometida.
- No borres rastros ni “limpies” equipos sin preservar evidencias.
- Aísla segmentos, servidores y credenciales sospechosas.
- Suspende cambios no esenciales.

El objetivo es evitar propagación y proteger activos críticos.

## 3) Proteger las funciones críticas de negocio
Clasifica inmediatamente:
- Qué servicios están caídos
- Qué servicios siguen operativos
- Qué procesos críticos deben mantenerse por obligación regulatoria o contractual
- Qué alternativas manuales o degradadas existen

En pagos, normalmente hay que decidir:
- Qué operaciones se pueden pausar
- Qué operaciones deben pasar a modo degradado/manual
- Qué límites temporales aplicar
- Qué canales deben cerrarse preventivamente

## 4) Ejecutar continuidad de negocio
Activa BCP/DRP si existe:
- Procedimientos manuales para pagos críticos
- Priorización de clientes vulnerables o transacciones urgentes
- Colas de procesamiento diferido
- Canales alternativos
- Acuerdos con terceros/proveedores críticos

La pregunta no es solo “cómo volver”, sino “qué servicio mínimo seguro podemos prestar ya”.

## 5) Preservar evidencia y entender el alcance
Pide al equipo técnico/forense que determine con urgencia:
- Alcance del compromiso
- Sistemas afectados y no afectados
- Si hay exfiltración de datos
- Si hay compromiso de identidades privilegiadas
- Si backups, AD, EDR, correo o herramientas de administración están afectados
- Hora estimada de inicio y vector de entrada

Esto condiciona cualquier recuperación.

## 6) Gestionar obligaciones regulatorias y legales
En una entidad financiera esto es crítico:
- Informa de inmediato a Legal/Compliance.
- Evalúa notificación a supervisor financiero, autoridad de protección de datos, CERT nacional y otras autoridades aplicables.
- Revisa obligaciones contractuales con clientes y terceros.
- Documenta todas las decisiones y tiempos.

No esperes a tener todos los detalles para activar el circuito regulatorio interno.

## 7) Comunicación clara y controlada
Prepara tres líneas de comunicación:
### Interna
- Qué se sabe
- Qué no se sabe
- Qué deben hacer los empleados
- Qué no deben hacer

### Clientes
- Reconocer incidencia
- Explicar impacto funcional, no especular
- Dar alternativas temporales
- Comprometer próxima actualización con hora concreta

### Reguladores / socios / terceros críticos
- Estado
- Impacto
- Medidas de contención
- Próximos hitos

Evita mensajes técnicos no confirmados o promesas de recuperación no validadas.

## 8) Criterio para restaurar servicio
La restauración debe aprobarse solo cuando Seguridad, TI y negocio confirmen:
- El entorno de recuperación está limpio
- El vector de acceso está contenido
- Las credenciales comprometidas han sido tratadas
- Hay monitorización reforzada
- El servicio puede operar con riesgo residual aceptado formalmente

Restaurar demasiado pronto puede provocar reinfección y una caída peor.

## 9) Decisiones de negocio que debes liderar tú
Como responsable de negocio, céntrate en decidir:
- Servicios prioritarios por impacto económico y social
- Umbral de servicio mínimo aceptable
- Segmentos de clientes prioritarios
- Tolerancia temporal a operación manual/degradada
- Mensaje a clientes y red comercial
- Escalado a dirección y consejo si aplica

## 10) Qué pedir en los próximos 30 minutos
Solicita un briefing ejecutivo con este formato:
- Qué ha pasado
- Qué sistemas están afectados
- Qué impacto real hay en clientes y operaciones
- Qué se ha aislado ya
- Riesgo de propagación
- Riesgo de fuga de datos
- Opciones de continuidad disponibles hoy
- ETA por escenarios: conservador / probable / optimista
- Decisiones que negocio debe tomar ahora

## 11) Qué no hacer
- No forzar vuelta a producción sin validación de seguridad.
- No pagar ni negociar sin intervención legal, ejecutiva y especializada.
- No comunicar causas no confirmadas.
- No permitir accesos extraordinarios sin control.
- No mezclar recuperación técnica con presión comercial sin gobierno de crisis.

## Mensaje ejecutivo recomendado
Puedes usar algo así internamente:

> “Tratamos la incidencia como un posible ciberincidente grave. La prioridad es contener, preservar evidencia y mantener el servicio mínimo seguro a clientes críticos. No se autorizará restauración de sistemas hasta validar alcance, integridad del entorno y riesgo residual. Activamos comité de crisis, continuidad de negocio, comunicación controlada y evaluación regulatoria inmediata.”

Si quieres, puedo ayudarte ahora mismo con uno de estos tres entregables:
1. un checklist ejecutivo para la próxima hora,
2. un guion de comité de crisis para una entidad financiera,
3. un borrador de comunicación a clientes y regulador.