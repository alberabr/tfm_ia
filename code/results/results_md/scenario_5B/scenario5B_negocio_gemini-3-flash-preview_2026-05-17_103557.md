Esta es una situación de **Gestión de Crisis de Nivel 1**. Como responsable de negocio, tu prioridad es triple: **contener el daño financiero, proteger al cliente y preservar la reputación a largo plazo.**

El mayor error en estos casos es el silencio por miedo al pánico. En banca, la falta de información se interpreta como falta de control.

Aquí tienes una hoja de ruta de actuación inmediata dividida por áreas:

### 1. Acción Inmediata: El "War Room" (Comité de Crisis)
Convoca en los próximos 15 minutos a los responsables de: **Seguridad (CISO), Legal/Cumplimiento, Atención al Cliente y Comunicación.**

*   **Objetivo:** Centralizar la información. No puede haber mensajes contradictorios.
*   **Decisión técnica urgente:** Evaluar si es necesario el bloqueo temporal de transferencias salientes sospechosas o el reseteo forzado de credenciales para usuarios que hayan accedido desde IPs vinculadas al phishing.

### 2. Mitigación Operativa (Frenar la sangría)
*   **Takedown del sitio:** Seguridad debe estar ya trabajando con proveedores de inteligencia de amenazas para dar de baja la web fraudulenta.
*   **Refuerzo en el Call Center:** Si recibes 5 reclamaciones por minuto, tu centralita colapsará en breve. Desvía personal de otras áreas para triaje inicial.
*   **Protocolo de "Stop Payment":** Automatiza, en la medida de lo posible, la retención de operaciones denunciadas que aún no hayan sido liquidadas (compensación bancaria).

### 3. Estrategia de Comunicación (El equilibrio delicado)
No esperes a tener el número total de afectados para hablar. La clave es **comunicar prevención, no solo el desastre.**

*   **Comunicación Proactiva General (Preventiva):** Envía un mensaje (Push en App, SMS y Email) a **toda** la base de clientes.
    *   *El mensaje:* "Aviso de seguridad: Detectada campaña de suplantación. Recuerde que [Nombre de la Entidad] NUNCA le pedirá sus claves por SMS o enlace. Si ha introducido sus datos en una web sospechosa, llame al [Número]."
    *   *Por qué esto no daña la reputación:* Demuestra que el banco vigila y protege. El cliente prefiere un banco "pesado" con la seguridad que uno que permite que le roben.
*   **Comunicación Segmentada (Afectados):** A medida que identifiquéis cuentas comprometidas, bloquead el acceso online y contactad individualmente.

### 4. Gestión de la Confianza y Reputación
Para evitar la fuga de clientes, la respuesta sobre el dinero es vital:

*   **Política de Reembolsos:** Si las operaciones no han tenido doble factor de autenticación (SCA) robusto o si el cliente fue engañado por una técnica sofisticada, aclara internamente (y luego externamente) la política de devolución. Bajo la normativa **PSD2**, la responsabilidad suele recaer en la entidad si no se demuestra negligencia grave del cliente.
*   **Transparencia:** Una vez controlada la entrada de nuevos afectados, emite un comunicado oficial asumiendo la situación, explicando las medidas tomadas y reforzando el compromiso con la seguridad.

### 5. Cumplimiento Legal y Regulatorio
*   **Notificación a las Autoridades:** Tienes plazos legales (72h para el RGPD si hay fuga de datos personales) para informar a la Agencia de Protección de Datos y al regulador financiero (Banco Central).
*   **Denuncia policial:** Coordinar con el equipo legal una denuncia conjunta por la campaña de phishing.

### Resumen de prioridades para TI ahora mismo:
1.  **Bloquear** el acceso a la URL fraudulenta desde vuestra red.
2.  **Identificar** patrones comunes en las reclamaciones (¿vienen todas de un mismo enlace SMS?).
3.  **Monitorizar** salidas de fondos inusuales en tiempo real.

**Mi consejo como consultor:** El miedo a la "alarma" suele causar retrasos que multiplican el número de víctimas. **Es mejor pedir disculpas por una alerta de seguridad preventiva que dar explicaciones por miles de cuentas vaciadas.** La reputación se recupera con una gestión eficiente de la crisis, no ocultándola.