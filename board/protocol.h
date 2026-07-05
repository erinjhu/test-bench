#ifndef PROTOCOL_H
#define PROTOCOL_H

#include <stdint.h>

// Constants
#define SOF_BYTE 0xAA

// Command IDs
typedef enum {
    /* Read */
    INVALID_GET = NULL,
    CMD_PING      = 0x01,
    CMD_GET_VOLT  = 0x02, 
    /* Write */
    INVALID_SET = NULL,
    CMD_SET_PWM   = 0x03 
} CommandID;

// Packet
typedef struct {
    uint8_t sof; /* Start of frame*/
    uint8_t cmd_id;
    uint8_t len;
    uint8_t* payload;
    uint8_t checksum;
} Packet;

#endif