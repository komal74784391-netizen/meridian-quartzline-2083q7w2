# Quartzline design notes

Pipelines are composed of pure feature steps. Streaming mode buffers 256 rows
before emitting feature batches.
