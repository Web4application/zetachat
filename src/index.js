import { DurableObject } from "cloudflare:workers";

type Session = { id: string; user_id: string; created_at: number };
type PromptHistory = {
  id: string;
  session_id: string;
  role: string;
  content: string;
};

export class AgentHistory extends DurableObject {
  async getSessionContext(sessionId: string) {
    // All queries execute with zero network latency — compute and data are colocated
    const session = this.ctx.storage.sql
      .exec<Session>("SELECT * FROM sessions WHERE id = ?", sessionId)
      .one();
    const prompts = this.ctx.storage.sql
      .exec<PromptHistory>(
        "SELECT * FROM prompt_history WHERE session_id = ? ORDER BY created_at",
        sessionId,
      )
      .toArray();

    return { session, prompts };
  }
}
