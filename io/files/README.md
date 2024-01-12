# io/files

**Disk (or tape) routines**

## Error codes

| Code | Description | Routine |
| ---- | ----------- | ------- |
| 01 | Maximum number of files already open exceeded | OPEN |
| 02 | File handler in use | OPEN |
| 03 | File not open | CHKIN CHKOUT |
| 05 | Device did not respond / device not present | OPEN |
| 04 | File not found / Short block (TAPE) | CHKIN CHKOUT |
| 08 | Long block (TAPE) | CHKIN CHKOUT |
| 10 | Unrecoverable read error | CHKIN CHKOUT  |

For further information, the drive error channel has to be read.
