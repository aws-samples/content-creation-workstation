# ChangeLog for Content Creation Workstation

## [0.1.7] - 2020-08-14

### Added

- Added: AWS Solution project files and modified directory structure as recommended.

## [0.1.6] - 2020-07-21

### Added

- Added: VPC Flow Logs Option
- Added: Feature to have ability to enable termination protection on EC2 instance.
- Added: Feature to create S3 bucket for file storage and sync it with VFX Host.
- Added: Windows now has AWS CLI Downloaded onto the instance.
- Added: IAM role for EC2 instance to have ability to talk to the S3 bucket. (least privilege).

### Removed

- Removed: FTP Server functionality.

## [0.1.5] - 2020-06-11

### Fixed/Updated

- Fixed: Client VPN Bug: Client VPN Route error when creating new Client VPN endpoint on a new VPC.
- Fixed: Blender Installation Bug: Blender Installation failure when downloading Blender 2.82. Updated to use chocolatey for download.
- Updated: "CreateVPNEndpoint" parameter to only allow values 'true'  and 'false'
- Updated: cfn-init to leverage Powershell file for the cfn-init process.
- Updated: Reference architecture to reflect current installation progress.
- Updated: Updated README.md

### Added

- Added: Scripts to install Wacom drivers on Windows VFX host.

### Removed

- Removed: Unneeded Architecture Diagram Pictures.

## [0.1.4] - 2020-06-05

### Added

- Added: Name to VFX Host
- Added: Description to Security Group inbound rules.

## [0.1.3] - 2020-05-30

### Added

- Added: FTP Server to Windows VFX Host

## [0.1.2] - 2020-05-29

### Added

- Added: FTP Server to Linux VFX Host

## [0.1.1] - 2020-05-19

### Added

- Added:Reference Architecture.

### Removed

- Added: FSx Lustre Resources.

## [0.1.0] - 2020-05-15

### Added

- Initial solution for deploying Teradici Cloud Access on CentOS or Windows 2019 EC2 instances.
- Architectural Diagrams in README
- Client VPN Endpoint Resources
- FSx for Lustre Resrouces
- Additional Security Group, IAM Role and other AWS Resources.
