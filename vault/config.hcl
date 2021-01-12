disable_cache = true
disable_mlock = true

log_level = "Trace"

storage "file" {
  path = "/mnt/vault/data"
}

listener "tcp" {
  address     = "127.0.0.1:8200"
  tls_disable = 1
}
