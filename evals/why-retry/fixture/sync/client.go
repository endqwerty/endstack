package sync

import (
	"math/rand"
	"net/http"
	"time"
)

const maxRetries = 7
const baseBackoff = 250 * time.Millisecond

func backoff(attempt int) time.Duration {
	d := baseBackoff << attempt
	return d/2 + time.Duration(rand.Int63n(int64(d/2)))
}

func shouldRetry(resp *http.Response) bool {
	return resp != nil && resp.StatusCode == http.StatusServiceUnavailable
}
