# Access Control System

## Overview
This document describes the comprehensive access control system implemented using Role-Based Access Control (RBAC) and Row-Level Security (RLS) in the vns-masakinihirota application.

## Architecture

### Components
- **Supabase RLS Policies**: Database-level security enforcing access rules
- **Permission Helpers**: Server-side functions for checking user permissions
- **Auth Context**: Client-side React context for user state management
- **Server Actions**: Next.js server actions with permission validation
- **Conditional UI**: Components that render based on user permissions

### Database Schema
The system uses the following tables:
- `roles`: Defines available roles (admin, moderator, user, etc.)
- `user_role_assignments`: Links users to their roles
- `groups`: User-created groups
- `group_members`: Group membership with roles
- `profile_relationships`: User relationships (follows, blocks, etc.)
- `hierarchy_applications`: Group hierarchy applications

## Permission System

### Server-Side Permissions (`src/lib/auth/permissions.ts`)
```typescript
// Check if user has a specific role
hasRole(userId: string, roleName: string): Promise<boolean>

// Check if user is group leader
checkGroupLeader(userId: string, groupId: string): Promise<boolean>

// Get user profile with permissions
getCurrentProfile(userId: string): Promise<UserProfile | null>
```

### Client-Side Auth Context (`src/contexts/AuthContext.tsx`)
```typescript
const { profile, isLeader, hasRole } = useAuth();
```

## Usage Examples

### Server Action with Permissions
```typescript
'use server'
import { checkGroupLeader } from '@/lib/auth/permissions';

export async function updateGroupSettings(groupId: string, settings: any) {
  const profile = await getCurrentProfile();
  if (!profile || !await checkGroupLeader(profile.id, groupId)) {
    throw new Error('Unauthorized');
  }
  // Update logic
}
```

### Conditional UI Component
```typescript
import { useAuth } from '@/contexts/AuthContext';

export function GroupSettingsButton({ groupId }: { groupId: string }) {
  const { isLeader } = useAuth();

  if (!isLeader(groupId)) return null;

  return <button>Settings</button>;
}
```

## Testing
The system includes comprehensive tests:
- Permission helper functions
- Auth context behavior
- Component rendering based on permissions
- RLS policy validation (requires Supabase local setup)

Run tests with: `pnpm vitest run --coverage`

## Security Considerations
- All database operations use RLS policies
- Server-side permission checks prevent client-side bypass
- Service role used for administrative operations
- User input validated before permission checks

## Future Enhancements
- Fine-grained permissions per resource
- Permission caching for performance
- Audit logging for security events
- Integration with external auth providers
