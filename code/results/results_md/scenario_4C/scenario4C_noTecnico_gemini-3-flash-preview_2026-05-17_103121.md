Esta es una situación crítica que debe tratarse como un **Incidente de Seguridad de Alto Impacto**. En el sector bancario, la rapidez y el cumplimiento de los protocolos son esenciales para mitigar daños legales, reputacionales y financieros.

Aquí tienes una guía de pasos inmediatos sobre qué hacer y a quién avisar:

### 1. ¿A quién avisar de inmediato? (Escalada)

No intentes resolverlo solo ni lo mantengas en un círculo pequeño. Debes activar los canales oficiales:

*   **CISO (Chief Information Security Officer) o Departamento de Seguridad de la Información:** Es el primer contacto. Ellos activarán el Plan de Respuesta a Incidentes.
*   **SOC (Security Operations Center):** Si el banco tiene un centro de monitoreo 24/7, deben ser informados para que empiecen a rastrear el origen de las conexiones y el tráfico de red.
*   **Departamento de Riesgos y Cumplimiento (Compliance):** Dado que hay cuentas de administrador involucradas, existe un riesgo legal y regulatorio (como el cumplimiento de la normativa de protección de datos o leyes bancarias).
*   **Tu superior directo:** Para que esté al tanto de que se están siguiendo protocolos de emergencia.

### 2. ¿Qué hacer con las cuentas de administrador?

El argumento de que "no conviene bloquearlas porque se usan para tareas importantes" es un **riesgo inaceptable** durante una brecha activa. Los atacantes suelen usar cuentas de servicio o de administrador precisamente porque nadie se atreve a tocarlas.

*   **Prioriza la Seguridad sobre la Operatividad:** Si una cuenta de administrador está comprometida, el atacante tiene "las llaves del reino". Puede borrar logs, crear nuevas cuentas, exfiltrar datos de clientes o plantar ransomware.
*   **Acción recomendada:** En lugar de un bloqueo total que detenga el servicio, el equipo de seguridad debe realizar un **cambio de credenciales inmediato** (reset de contraseña) y forzar el cierre de todas las sesiones activas.
*   **Implementar MFA:** Si esas cuentas no tienen autenticación de doble factor, debe activarse de inmediato.

### 3. Acciones de contención y análisis

Mientras los equipos técnicos trabajan, asegúrate de que se sigan estos pasos:

*   **No apagues los equipos afectados:** Si apagas un servidor o PC, se pierde la información volátil (memoria RAM) que sirve para la investigación forense. Es mejor desconectarlos de la red (quitar el cable o desactivar el Wi-Fi) si es necesario aislarlos.
*   **Identificar el alcance:** El equipo de IT debe revisar los logs de acceso para ver a qué bases de datos o archivos se accedió. Si se accedió a información de clientes (DNI, saldos, números de cuenta), esto cambia la gravedad del asunto.
*   **Revisar "Movimientos Laterales":** Los atacantes rara vez se quedan en un solo sistema. Una vez que entran con una cuenta de administrador, saltan a otros servidores.

### 4. Impacto en los Clientes y Obligaciones Legales

Como empleado bancario, debes saber que existen leyes estrictas (como el **RGPD** en Europa o normativas locales de supervisión bancaria):

*   **Notificación a las autoridades:** Si se confirma que se ha accedido a datos sensibles de clientes, el banco suele tener un plazo máximo (generalmente **72 horas**) para informar a la autoridad de protección de datos y al regulador bancario (ej. Banco de España, CNMV, etc.).
*   **Comunicación a clientes:** Si el riesgo para los clientes es alto (ej. robo de credenciales de banca online), el banco está obligado a informarles para que cambien sus claves o tomen medidas preventivas.

### 5. Lo que NO debes hacer

*   **No intentes "investigar" por tu cuenta:** Podrías alterar pruebas forenses necesarias para una denuncia policial posterior.
*   **No alertes al atacante:** Si sospechas que el acceso es interno (un empleado), no comentes tus sospechas de forma abierta; deja que el equipo de seguridad haga el seguimiento de forma silenciosa para identificar al responsable.
*   **No ignores las alertas:** El hecho de que "algunos equipos" digan que no conviene bloquear cuentas sugiere que hay una resistencia interna que puede estar facilitando el ataque. La seguridad debe prevalecer.

**Resumen de urgencia:** Contacta ahora mismo con el **Responsable de Seguridad de la Información (CISO)** o el **Canal de Denuncias/Incidencias Técnicas** de tu entidad y solicita que se inicie el protocolo de respuesta a incidentes de forma oficial.