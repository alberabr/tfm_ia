Esta es una situación de **prioridad alta (P1)**, especialmente tratándose de una entidad financiera. Al estar involucradas cuentas con privilegios elevados, el riesgo de movimiento lateral, persistencia y exfiltración de datos es crítico.

Debes seguir un protocolo de **Respuesta a Incidentes (IR)** estructurado (basado en marcos como NIST SP 800-61 o SANS). Aquí tienes los pasos inmediatos que deberías seguir:

---

### 1. Contención Inmediata (Frenar el impacto)
No esperes a tener toda la información para actuar sobre las cuentas comprometidas.
*   **Inhabilitar cuentas afectadas:** Deshabilita temporalmente las cuentas de usuario que han mostrado actividad sospechosa. No solo cambies la contraseña; cierra las sesiones activas (kill sessions).
*   **Bloqueo de red:** Bloquea las direcciones IP de origen sospechosas en el firewall o WAF.
*   **Aislamiento de sistemas:** Si es posible y no afecta la continuidad crítica del negocio, aísla los sistemas a los que se accedió de la red principal (segmentación) para evitar el movimiento lateral.
*   **Revisión de MFA:** Si las cuentas tenían MFA, investiga si hubo "MFA Fatigue" (bombardeo de notificaciones) o si el atacante logró saltarse el segundo factor (SIM swapping, robo de tokens).

### 2. Análisis y Diagnóstico (Identificar el alcance)
Debes determinar qué hizo el atacante mientras estuvo dentro.
*   **Análisis de Logs (SIEM/EDR):**
    *   Revisa logs de autenticación (Active Directory, Azure AD, Okta).
    *   Busca eventos de creación de nuevas cuentas (persistencia).
    *   Busca cambios en políticas de seguridad o reglas de firewall.
*   **Búsqueda de Movimiento Lateral:** Revisa si desde esos sistemas se intentó acceder a bases de datos, servidores de archivos o el core bancario.
*   **Integridad de Archivos (FIM):** Verifica si se han modificado archivos de configuración del sistema o binarios.
*   **Exfiltración de datos:** Revisa los logs de salida de red (NetFlow) para ver si hubo picos de transferencia de datos hacia el exterior en los horarios de las conexiones sospechosas.

### 3. Erradicación
Una vez contenido, elimina el rastro del atacante.
*   **Limpieza de persistencia:** Busca tareas programadas, nuevos servicios, llaves SSH añadidas o scripts de inicio que el atacante haya podido dejar.
*   **Reset de credenciales en cascada:** Si una cuenta de administrador fue comprometida, asume que todas las credenciales que residían en ese servidor podrían estar comprometidas (volcado de memoria LSASS). Considera un cambio de contraseñas masivo para cuentas privilegiadas.
*   **Parcheado:** Si el acceso se logró explotando una vulnerabilidad, aplica el parche inmediatamente antes de volver a poner el sistema en línea.

### 4. Comunicación y Cumplimiento (Crítico en Sector Financiero)
Como entidad financiera, tienes obligaciones legales estrictas.
*   **Escalada interna:** Notifica al CISO, al departamento legal y al de Riesgos.
*   **Notificación regulatoria:** Dependiendo de tu país, podrías tener un plazo limitado (ej. 72 horas bajo GDPR en Europa, o plazos específicos de reguladores bancarios como el Banco de España, CNMV, SEC, etc.) para informar si hay sospecha de robo de datos personales o financieros.
*   **Preservación de evidencia:** Si planeas tomar acciones legales o reclamar seguros de ciberriesgo, asegúrate de realizar copias forenses de los discos y memorias de los sistemas afectados antes de modificarlos.

### 5. Recuperación
*   **Restauración desde backups:** Si sospechas que el sistema fue alterado, es preferible restaurar una copia de seguridad limpia (previa al incidente) y aplicar los parches necesarios.
*   **Monitoreo intensivo:** Durante las próximas semanas, establece alertas de "umbral cero" para esas cuentas y sistemas.

---

**Preguntas clave que debes responder ahora mismo:**
1.  ¿Esas cuentas tienen acceso a datos de clientes (PII) o datos de tarjetas (PCI)?
2.  ¿Se han detectado ejecuciones de PowerShell, CMD o herramientas de hacking (Mimikatz, Cobalt Strike) en los endpoints?
3.  ¿Las conexiones sospechosas provienen de VPNs conocidas, nodos de salida Tor o países donde la entidad no opera?

**Recomendación proactiva:** Si no cuentas con un equipo de respuesta a incidentes (DFIR) interno con experiencia, considera contratar de inmediato un servicio externo de **Retainer de IR** para realizar el análisis forense profundo.