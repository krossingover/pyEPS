# Source: 24.301 v12.2.0, Section 9.1
# 1)    if the message is a plain NAS message:
#    a)    protocol discriminator;
#    b)    EPS bearer identity or security header type;
#    c)    procedure transaction identity;
#    d)    message type;
#    e)    other information elements, as required.
# 2)    if the message is a security protected NAS message:
#    a)    protocol discriminator;
#    b)    security header type;
#    c)    message authentication code;
#    d)    sequence number;
#    e)    plain NAS message, as defined in item 1.

# The EPS bearer identity and the procedure transaction identity are only used in messages with protocol discriminator EPS session management. 


attachRequest = lambda epsAttachType, nasKeySetIdentifier, epsMobileIdentity, ueNetworkCapability, esmMessage: (
    "nas",
    {
     },
    {
     "protocolDiscriminator": "EpsMobilityManagementMessage",
     "messageType": "attachRequest",
     "securityHeaderType": "plainNasMessage",
     "epsAttachType": epsAttachType,
     "nasKeySetIdentifier": nasKeySetIdentifier,
     "epsMobileIdentity": epsMobileIdentity,
     "ueNetworkCapability": ueNetworkCapability,
     "esmMessageContainer": esmMessage
     }
)

attachAccept = lambda sequenceNumber, taiList, guti, esmMessage: (
    "nas",
    {
     },
    {
     "protocolDiscriminator": "EpsMobilityManagementMessage",
     "sequenceNumber": sequenceNumber,
     "messageType": "attachAccept",
     "securityHeaderType": "securityProtectedNasMessage",
     "taiList": taiList,
     "guti": guti,
     "esmMessageContainer": esmMessage
     }
)

attachComplete = lambda sequenceNumber, esmMessage: (
    "nas",
    {
     },
    {
     "protocolDiscriminator": "EpsMobilityManagementMessage",
     "sequenceNumber": sequenceNumber,
     "messageType": "attachComplete",
     "securityHeaderType": "securityProtectedNasMessage",
     "esmMessageContainer": esmMessage
     }
)

pdnConnectivityRequest = \
    lambda epsBearerIdentity, procedureTransactionIdentity, requestType, pdnType, accessPointName: (
        "nas",
        {
         },
        {
        "protocolDiscriminator": "EpsSessionManagementMessage",
         "messageType": "pdnConnectivityRequest",
         "epsBearerIdentity": epsBearerIdentity,
         "procedureTransactionIdentity": procedureTransactionIdentity,
         "requestType": requestType,
         "pdnType": pdnType,
         "accessPointName": accessPointName     
         }                                                                                                                                                                                          
)

activateDefaultEpsBearerContextRequest = \
    lambda epsBearerIdentity, procedureTransactionIdentity, epsQualityOfService, accessPointName, pdnAddress, apnAmbr: (
        "nas",
        {
        },
        {
         "protocolDiscriminator": "EpsSessionManagementMessage",
         "epsBearerIdentity": epsBearerIdentity,
         "procedureTransactionIdentity": procedureTransactionIdentity,
         "messageType": "activateDefaultEpsBearerContextRequest",
         "epsQualityOfService": epsQualityOfService,
         "accessPointName": accessPointName,
         "pdnAddress": pdnAddress,
         "apnAmbr": apnAmbr     
         }                                                                                                                                                                                          
)

activateDefaultEpsBearerContextAccept = \
    lambda epsBearerIdentity, procedureTransactionIdentity: (
        "nas",
        {
        },
        {
         "protocolDiscriminator": "EpsSessionManagementMessage",
         "epsBearerIdentity": epsBearerIdentity,
         "procedureTransactionIdentity": procedureTransactionIdentity,
         "messageType": "activateDefaultEpsBearerContextAccept",
         }                                                                                                                                                                                          
)