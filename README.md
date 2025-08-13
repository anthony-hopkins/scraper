# Web Scraper - Offline Website Downloader

A Python-based web scraping tool designed to download websites in their entirety for offline viewing. This application processes a newline-delimited list of URLs and downloads each page locally, making it perfect for offline research, archiving, and analysis purposes.

## 🚀 Features

- **Batch URL Processing** - Download multiple websites from a URL list
- **Offline Viewing** - Save complete web pages for offline access
- **Simple Interface** - Command-line tool with minimal dependencies
- **Error Handling** - Graceful handling of invalid URLs and redirects
- **Local Storage** - Organized file naming with incremental counters
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Lightweight** - Minimal Python dependencies, no external libraries

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.6+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Text editor for creating URL lists

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd scraper
```

### 2. Prepare Your URL List

Create a text file with URLs (one per line):

```bash
# Create urllist.txt
echo "http://example.com/" > urllist.txt
echo "https://another-site.com/" >> urllist.txt
```

### 3. Run the Scraper

```bash
python3 scraper.py urllist.txt
```

### 4. View Downloaded Files

Check your current directory for downloaded HTML files:
- `URL_0.html` - First URL in your list
- `URL_1.html` - Second URL in your list
- And so on...

## 🏗️ Project Structure

```
scraper/
├── scraper.py                  # Main scraping application
├── urllist.txt                 # Example URL list file
└── README.md                   # This documentation
```

## 🔧 Configuration

### URL List Format

The URL list file should contain:
- **One URL per line**
- **Valid HTTP/HTTPS URLs**
- **No extra formatting or special characters**

Example `urllist.txt`:
```
http://example.com/
https://another-site.com/
http://third-site.org/
```

### Command Line Usage

```bash
python3 scraper.py <path_to_url_list>
```

**Arguments:**
- `path_to_url_list`: Full or relative path to your URL list file

## 📦 Dependencies

### Core Components

- **Python 3.6+** - Runtime environment
- **urllib** - Built-in Python library for URL handling
- **os** - Built-in Python library for file operations
- **sys** - Built-in Python library for command-line arguments

### No External Libraries Required

This scraper uses only Python standard library modules, making it:
- **Easy to deploy** - No pip install required
- **Lightweight** - Minimal memory footprint
- **Reliable** - No dependency conflicts

## 🐳 Usage Examples

### Basic Scraping

```bash
# Download websites from urllist.txt
python3 scraper.py urllist.txt
```

### Custom URL List

```bash
# Use a different URL list file
python3 scraper.py my_urls.txt
```

### Absolute Path

```bash
# Use absolute path to URL list
python3 scraper.py /home/user/websites.txt
```

## 🚀 Development Workflow

### Running the Scraper

```bash
# Check Python version
python3 --version

# Run scraper with URL list
python3 scraper.py urllist.txt

# Monitor output
tail -f scraper.log  # if logging is enabled
```

### Debugging

```bash
# Run with verbose output
python3 -v scraper.py urllist.txt

# Check file permissions
ls -la urllist.txt
```

## 🔍 Application Features

### URL Processing

- **Sequential Download** - Processes URLs one by one
- **Progress Tracking** - Shows download progress for each URL
- **Error Handling** - Continues processing even if individual URLs fail
- **File Naming** - Creates organized HTML files with incremental naming

### Download Management

- **Local Storage** - Saves files in current working directory
- **HTML Format** - Downloads complete web page content
- **Overwrite Protection** - Each run creates new numbered files
- **Directory Organization** - All files saved in one location

## 🚨 Important Notes

### Limitations

- **Not a Crawler** - Only downloads specified URLs, doesn't follow links
- **Redirect Handling** - May not work with complex redirects (Google, YouTube, Facebook)
- **JavaScript** - Dynamic content may not be captured
- **Authentication** - Protected pages may not be accessible

### Best Practices

- **Respect robots.txt** - Check website policies before scraping
- **Rate Limiting** - Add delays between requests for large lists
- **Legal Compliance** - Ensure scraping is allowed by target websites
- **Resource Management** - Monitor disk space for large downloads

## 🚀 Production Deployment

For production use, consider:

1. **Rate Limiting** - Add delays between requests
2. **User Agents** - Set appropriate browser identification
3. **Proxy Support** - Rotate IP addresses for large-scale scraping
4. **Logging** - Add comprehensive logging and monitoring
5. **Error Recovery** - Implement retry mechanisms for failed downloads
6. **Storage Management** - Implement file cleanup and archiving

## 🔧 Customization

### Adding Features

Extend the scraper by modifying `scraper.py`:

```python
# Example: Add user agent
headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyBot/1.0)'}

# Example: Add delay between requests
import time
time.sleep(1)  # 1 second delay
```

### Error Handling

Customize error handling for specific use cases:

```python
# Example: Specific error handling
try:
    # Download logic
except urllib.URLError as e:
    print(f"URL Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Scraping! 🕷️**
