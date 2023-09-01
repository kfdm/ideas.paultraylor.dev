---
title: iCalendar Notes
date: 2019-05-20T05:15:24.000Z
toc: true
tags:
  - caldav
  - icalendar
summary: iCalendar Exploration Notes
---

iCalendar Exploration Notes

<!--more-->


# Event Component

<code style="font-family: monospace; white-space: pre;">
BEGIN:VCALENDAR
VERSION:2.0
[PRODID]:-//Apple Inc.//Mac OS X 10.13.6//EN
CALSCALE:GREGORIAN
BEGIN:[VEVENT][VEVENT]
[TRANSP]\:TRANSPARENT
[DTEND];VALUE=DATE:20190521
[LAST-MODIFIED]\:20190520T051107Z
[UID]\:B5624828-2B4D-4066-A9A5-A85BFB7464BB
[DTSTAMP]\:20190520T051107Z
[DESCRIPTION]:# Goals\n- Some goals\n- Could go here\n# Like this\n- and t
 his\n\n[test]: http://google.com\n[inline](http://google.com)
X-APPLE-SCHEDULETAG:
X-APPLE-SERVERFILENAME:B5624828-2B4D-4066-A9A5-A85BFB7464BB.ics
[SEQUENCE]\:0
X-APPLE-EWS-BUSYSTATUS:FREE
[SUMMARY]:Worklog 2019-05-20
DTSTART;VALUE=DATE:20190520
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
[CREATED]\:20190520T050811Z
X-APPLE-ETAG:"b74937ed76f319494d75058916d8c275"
[CATEGORIES]\:APPOINTMENT,EDUCATION
END:VEVENT
END:VCALENDAR
</code>

# To-Do Component

<code style="font-family: monospace; white-space: pre;">
BEGIN:[VTODO][VTODO]
[UID]\:20070514T103211Z-123404@example.com
[DTSTAMP]\:20070514T103211Z
[DTSTART]\:20070514T110000Z
[DUE]\:20070709T130000Z
[COMPLETED]\:20070707T100000Z
[SUMMARY]:Submit Revised Internet-Draft
[PRIORITY]\:1
[STATUS]\:NEEDS-ACTION
[CATEGORIES]\:APPOINTMENT,EDUCATION
END:VTODO
</code>

# Journal Component

<code style="font-family: monospace; white-space: pre;">
BEGIN:[VJOURNAL][VJOURNAL]
[UID]\:19970901T130000Z-123405@example.com
[DTSTAMP]\:19970901T130000Z
[DTSTART]\;VALUE=DATE:19970317
[SUMMARY]\:Staff meeting minutes
[DESCRIPTION]:1. Staff meeting: Participants include Joe\,
    Lisa\, and Bob. Aurora project plans were reviewed.
    There is currently no budget reserves for this project.
    Lisa will escalate to management. Next meeting on Tuesday.\n
2. Telephone Conference: ABC Corp. sales representative
    called to discuss new printer. Promised to get us a demo by
    Friday.\n3. Henry Miller (Handsoff Insurance): Car was
    totaled by tree. Is looking into a loaner car. 555-2323
    (tel).
END:VJOURNAL
</code>


[COMPLETED]: https://tools.ietf.org/html/rfc5545#section-3.8.2.1
[CREATED]: https://tools.ietf.org/html/rfc5545#section-3.8.7.1
[DESCRIPTION]: https://tools.ietf.org/html/rfc5545#section-3.8.1.5
[DTEND]: https://tools.ietf.org/html/rfc5545#section-3.8.2.2
[DTSTAMP]: https://tools.ietf.org/html/rfc5545#section-3.8.7.2
[DTSTART]: https://tools.ietf.org/html/rfc5545#section-3.8.2.4
[DUE]: https://tools.ietf.org/html/rfc5545#section-3.8.2.3
[LAST-MODIFIED]: https://tools.ietf.org/html/rfc5545#section-3.8.7.3
[PRIORITY]: https://tools.ietf.org/html/rfc5545#section-3.8.1.9
[PRODID]: https://tools.ietf.org/html/rfc5545#section-3.7.3
[SEQUENCE]: https://tools.ietf.org/html/rfc5545#section-3.8.7.4
[STATUS]: https://tools.ietf.org/html/rfc5545#section-3.8.1.11
[SUMMARY]: https://tools.ietf.org/html/rfc5545#section-3.8.1.12
[TRANSP]: https://tools.ietf.org/html/rfc5545#section-3.8.2.7
[UID]: https://tools.ietf.org/html/rfc5545#section-3.8.4.7
[VEVENT]: https://tools.ietf.org/html/rfc5545#section-3.6.1
[VJOURNAL]: https://tools.ietf.org/html/rfc5545#section-3.6.3
[VTODO]: https://tools.ietf.org/html/rfc5545#section-3.6.2
[CATEGORIES]: https://tools.ietf.org/html/rfc5545#section-3.8.1.2