#!/bin/sh
set -eu

BASE_URL="${BASE_URL:-http://127.0.0.1:5000}"

health_response=$(curl --connect-timeout 1 --max-time 2 --fail --silent --show-error "$BASE_URL/health")
[ "$health_response" = '{"status":"ok"}' ] || {
    printf 'Unexpected health response: %s\n' "$health_response" >&2
    exit 1
}

fine_response=$(curl --connect-timeout 1 --max-time 2 --fail --silent --show-error "$BASE_URL/fine?days=5")
[ "$fine_response" = '{"fee":1.5}' ] || {
    printf 'Unexpected fine response: %s\n' "$fine_response" >&2
    exit 1
}

deluxe_response=$(curl --connect-timeout 1 --max-time 2 --fail --silent --show-error "$BASE_URL/fine?days=5&deluxe=1")
[ "$deluxe_response" = '{"fee":3.0}' ] || {
    printf 'Unexpected deluxe response: %s\n' "$deluxe_response" >&2
    exit 1
}

printf 'Smoke checks passed\n'