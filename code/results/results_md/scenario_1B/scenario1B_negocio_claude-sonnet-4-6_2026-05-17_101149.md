# Gestión de Incidente de Ransomware en Plataforma de Pagos

Entiendo la urgencia. Voy a darte un marco estructurado y práctico.

---

## 🔴 FASE INMEDIATA (primeras horas) - Si no está hecho ya

### Contención
- **Aislar sistemas afectados** de la red sin apagarlos (preservar evidencias forenses)
- **No pagar el rescate** todavía - no garantiza recuperación y puede tener implicaciones legales
- Activar **equipo de respuesta a incidentes** (interno o externo especializado)
- Identificar el **vector de entrada** para evitar reinfección al restaurar

### Activación de protocolos
- Declarar formalmente el **incidente crítico** con un responsable único de coordinación
- Activar **plan de continuidad de negocio (BCP)** si existe
- Convocar **comité de crisis**: IT, Negocio, Legal, Comunicación, Dirección

---

## ⚖️ OBLIGACIONES REGULATORIAS - Crítico en banca

### Notificaciones obligatorias (con plazos estrictos)
| Organismo | Plazo | Base |
|-----------|-------|------|
| **Banco de España** | Inmediato/horas | Circular de resiliencia operativa |
| **CNPD/AEPD** | 72 horas | RGPD si hay datos personales comprometidos |
| **CNPV / CCN-CERT** | Según clasificación | Esquema Nacional de Seguridad |
| **DORA** | Según severidad | Si aplica (desde enero 2025) |

> ⚠️ **No notificar en plazo puede ser más grave que el incidente mismo**

---

## 🔧 RECUPERACIÓN DEL SERVICIO

### Secuencia recomendada
1. **Validar backups** - integridad y que no estén comprometidos
2. **Entorno limpio** - no restaurar sobre infraestructura potencialmente infectada
3. **Priorizar** la plataforma de pagos sobre otros sistemas
4. **Pruebas antes de reconectar** - verificar que el malware no persiste
5. **Monitorización intensiva** post-restauración

### Alternativas mientras se recupera
- ¿Existe **sistema alternativo o contingencia** para pagos críticos?
- Procesamiento **manual temporal** para operaciones prioritarias
- Coordinación con **corresponsales o redes de pago** alternativas

---

## 📢 GESTIÓN DE CLIENTES Y REPUTACIÓN

### Comunicación (honesta y controlada)
- **Mensaje claro y único** - evitar contradicciones entre canales
- Informar **qué está afectado, qué no, y qué se está haciendo**
- Actualizar con **frecuencia definida** aunque no haya novedades
- Habilitar **canal de atención específico** para incidencia

### Lo que NO hacer
- ❌ Silencio prolongado
- ❌ Minimizar públicamente antes de conocer el alcance real
- ❌ Prometer tiempos de recuperación sin certeza técnica

---

## 🔍 PARALELO: Investigación forense

- Preservar logs y evidencias **antes de restaurar**
- Identificar si hubo **exfiltración de datos** (cambia el escenario legal)
- Determinar **tiempo de permanencia** del atacante en los sistemas
- Esto es necesario para el regulador y para evitar recurrencia

---

## 📋 PREGUNTAS CLAVE que deberías tener respondidas ahora

1. ¿Tenéis **backups validados y aislados**?
2. ¿Está activado el **BCP**?
3. ¿Se ha notificado ya al **Banco de España**?
4. ¿Hay **datos de clientes comprometidos**?
5. ¿Tenéis **seguro de ciberriesgo**? (actívalo ya)
6. ¿Hay un **único responsable** coordinando?

---

## Recursos especializados

- **CCN-CERT**: soporte a infraestructuras críticas (gratuito)
- **INCIBE-CERT**: +34 017
- Empresas especializadas: CrowdStrike, S21sec, Tarlogic, entre otras

---

¿En qué fase estáis exactamente? Puedo ayudarte a profundizar en la comunicación a clientes, la negociación con el regulador, o la secuencia técnica de recuperación según vuestra situación concreta.