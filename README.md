# VulnMatrix

VulnMatrix is a versatile Python-based port scanner and Common Vulnerabilities and Exposures (CVE) search tool. It scans a target server for open ports, identifies running services, and looks for known vulnerabilities associated with those services by searching the CVE database.

## Features

- Scans open ports on a target server.
- Identifies running services and software versions.
- Searches the CVE database for known vulnerabilities.
- Provides detailed information about identified vulnerabilities.

## Usage

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Run `VulnMatrix.py`.
3. Enter the target IP address when prompted.

VulnMatrix will initiate a port scan and service identification process. It will then search for known vulnerabilities in the identified services and display any relevant CVE information.

## Dependencies

- Python 3.x
- `requests` library for querying the CVE database

## Customization

- The `get_service_info` function in `VulnMatrix.py` is used to extract software version information from the services. You can customize this function based on your specific needs.
- The scanner currently targets common ports. You can modify the `target_ports` range to suit your requirements.

## Legal Considerations

- Ensure that you have proper authorization before scanning any server or network.
- Respect the terms of service and legal requirements when scanning external systems.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please contact **Ethan Prime** at **ethanprime.c137@protmail.com**.

---

**Disclaimer:** Use VulnMatrix responsibly and in compliance with applicable laws and regulations. The developers of VulnMatrix are not responsible for any misuse or illegal activities.
