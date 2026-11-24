terraform {
  required_version = ">= 1.0.0"
}
variable "environment" {
  default = "production"
}
variable "replicas" {
  default = 2
}
resource "null_resource" "capstone_infra_provisioner" {
  triggers = {
    env      = var.environment
    replicas = var.replicas
  }
  provisioner "local-exec" {
    command = "echo '[TERRAFORM IaC] Provisioned ${var.environment} cluster with ${var.replicas} replicas'"
  }
}
output "deployment_target" {
  value = "krmu-pulse-${var.environment}"
}
