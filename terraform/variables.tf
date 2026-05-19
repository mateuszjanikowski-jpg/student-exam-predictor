variable "service_name" {
  description = "Name of the Render web service"
  type        = string
  default     = "student-exam-predictor"
}

variable "repo_url" {
  description = "GitHub repository URL"
  type        = string
  default     = "https://github.com/mateuszjanikowski-jpg/student-exam-predictor"
}

variable "branch" {
  description = "Git branch used for deployment"
  type        = string
  default     = "main"
}