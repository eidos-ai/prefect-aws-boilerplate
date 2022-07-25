resource "aws_iam_role" "ecs_task_execution_role" {
  name = "${var.image_name}-TaskExecutionRole"
 
  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "ecs-tasks.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF
}

resource "aws_iam_role" "ecs_task_role" {
  name = "${var.image_name}-TaskRole"
 
  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "ecs-tasks.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF
}
 
resource "aws_iam_role_policy_attachment" "ecs-task-execution-role-policy-attachment" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
resource "aws_iam_role_policy_attachment" "task_s3" {
  role       = "${aws_iam_role.ecs_task_role.name}"
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}
resource "aws_ecs_task_definition" "definition" {
    family                   = "${var.image_name}-TaskDefinition"
    task_role_arn            = "arn:aws:iam::${var.aws_account_id}:role/${var.image_name}-TaskRole"
    execution_role_arn       = "arn:aws:iam::${var.aws_account_id}:role/${var.image_name}-TaskExecutionRole"
    network_mode             = "awsvpc"
    cpu                      = "${var.cpu}"
    memory                   = "${var.memory}"
    requires_compatibilities = ["FARGATE"]
    container_definitions    = jsonencode([
        {
        "image": "${var.aws_account_id}.dkr.ecr.${var.aws_region}.amazonaws.com/${var.image_name}:latest",
        "name": "flow"
        }
        ])
    }
    
