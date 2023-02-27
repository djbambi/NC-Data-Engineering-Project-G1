variable "loader_lambda_name" {
    type = string
    default = "loader"
}
variable "ingestion_lambda_name" {
    type = string
    default = "ingestion"
}
variable "transform_lambda_name" {
    type = string
    default = "transform"
}
variable "gen_lambda_name" {
    type = string
    default = "gen_lambda"
}

