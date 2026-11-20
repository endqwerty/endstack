export type RetryOptions = {
  maxAttempts: number;
  baseMs: number;
  capMs: number;
  random?: () => number;
  sleep?: (ms: number) => Promise<void>;
};

const realSleep = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms));

export function backoffMs(attempt: number, opts: RetryOptions): number {
  const random = opts.random ?? Math.random;
  const exp = Math.min(opts.capMs, opts.baseMs * 2 ** attempt);
  return exp + random() * opts.baseMs;
}

export async function withRetry<T>(fn: () => Promise<T>, opts: RetryOptions): Promise<T> {
  const sleep = opts.sleep ?? realSleep;
  let attempt = 0;
  for (;;) {
    try {
      return await fn();
    } catch (err) {
      attempt++;
      if (attempt > opts.maxAttempts) throw err;
      await sleep(backoffMs(attempt, opts));
    }
  }
}
