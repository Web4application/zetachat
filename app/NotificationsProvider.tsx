"use client";

import { ReactNode } from "react";
import { LiveblocksProvider } from "@liveblocks/react";

export function NotificationsProvider({ children }: { children: ReactNode }) {
  return (
    <LiveblocksProvider publicApiKey={"pk_prod_9KensGJpifraqw4oar3bVPl2T5Qh5W4NWUpdY0MwaUjA3RMH8gCLjfZyky9lyF77"}>
      {children}
    </LiveblocksProvider>
  );
}
