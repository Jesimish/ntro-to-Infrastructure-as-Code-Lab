# Define the provider (AWS)
provider "aws" {
   region = "us-west-2"
}

# Define the web server instance
resource "aws_instance" "web_server" {
   ami           = "ami-0c55b159cbfafe1f0"
   instance_type = "t2.micro"

# Attach the security group named web_server_sg to this EC2 instance
   vpc_security_group_ids = [aws_security_group.web_server_sg.id]

   tags = {
      Name = "WebServer"
      Environment = "Production"
   }
}

# instance = Resource type + rescource name + .id
# This assigns an Elastic IP
resource "aws_eip" "web_server_eip" {
  instance = aws_instance.web_server.id
}

# Define the security group for the webserver
resource "aws_security_group" "web_server_sg" {
   name_prefix = "web-server-sg-"

   ingress {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
   }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
