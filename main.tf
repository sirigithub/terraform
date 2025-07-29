# Define a large map with 1,000,000 key-value pairs
locals {
  large_map = { for i in range(1024) : "key_${i}" => "value_${i}" }
}

# Test lookup function
# output "lookup_result" {
#  value = lookup(local.large_map, "key_999999", "default_value")
# }

# Test try function
output "try_result" {
  value = try(local.large_map["key_999999"], "default_value")
}