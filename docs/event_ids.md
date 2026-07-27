# Windows and Sysmon Event IDs

## Purpose

This document describes the Windows Security and Sysmon Event IDs used throughout this project. Each Event ID includes its source, meaning, investigative value, and how it will be used by the analysis scripts.

---

# Windows Security Event IDs

## Authentication

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|
| 4624 | Successful logon | Windows Security | Records successful authentication. Useful for building timelines, identifying user activity, and detecting unexpected logins. |
| 4625 | Failed logon | Windows Security | Records failed authentication attempts. Useful for detecting password spraying, brute-force attacks, and invalid credential use. |
| 4634 | Logoff | Windows Security | Indicates that a user session ended. Helps determine session duration, correlate user activity, and identify when authenticated sessions terminate. |
| 4648 | Logon using explicit credentials | Windows Security | Indicates that a process attempted authentication using credentials different from the current user's. Useful for detecting tools such as `runas`, scheduled tasks, remote administration, and possible lateral movement. |
| 4672 | Special privileges assigned | Windows Security | Indicates that a successful logon received elevated privileges, such as administrative rights. Useful for identifying privileged account activity and investigating potential privilege escalation or unauthorized administrator access. |

## Process Creation

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|
| 4688 | Process creation | Windows Security | Records when a new process starts. Useful for identifying executed applications, reconstructing attack chains, analyzing parent-child process relationships, and detecting suspicious command-line activity. |

## Privilege Events

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|
| 4673 | Privileged service called | Windows Security | Records when a process requests sensitive system privileges. Useful for identifying privileged operations that may indicate administrative activity or attempted privilege escalation. |
| 4674 | Operation on a privileged object | Windows Security | Records attempts to perform operations on protected system objects. Useful for investigating access to sensitive resources and detecting potential abuse of elevated privileges. |
---

# Sysmon Event IDs

## Process Monitoring

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|
| 1 | Process creation | Sysmon | Records when a process starts with detailed information including command lines, parent processes, hashes, and execution context. Useful for detecting suspicious execution patterns and reconstructing attack chains. |
| 7 | Image loaded | Sysmon | Records when a process loads an executable image or DLL into memory. Useful for detecting suspicious DLL loading, identifying unsigned modules, and investigating code injection or execution techniques. |

## Network Monitoring

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|
| 3 | Network connection | Sysmon | Records network connections initiated by processes. Useful for identifying suspicious outbound communication, command-and-control activity, and correlating network behavior with process execution. |

## Registry Monitoring

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|

## File Monitoring

| Event ID | Meaning | Source | Why It Matters |
|----------|---------|--------|----------------|