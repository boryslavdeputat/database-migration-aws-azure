# DB cutover

1. Stop writes or enter freeze
2. Final lag = 0
3. Promote target / switch connection strings
4. Validate row counts + business checksums
5. Keep source read-only retention window
