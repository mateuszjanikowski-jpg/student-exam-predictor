resource "render_web_service" "student_exam_predictor" {
  name   = var.service_name
  plan   = "free"
  region = "frankfurt"

  runtime_source = {
    docker = {
      repo_url = var.repo_url
      branch   = var.branch
    }
  }
}