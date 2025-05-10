import os
import time

from playwright.sync_api import Page
from playwright.sync_api import expect
class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page

    # def download_csv(self):
    #     csv_download_btn = self.page.locator('.order-summary button').first
    #     # csv_download_btn = self.page.get_by_role("button", name="Click To Download Order Details in CSV")
    #     expect(csv_download_btn).to_have_text("Click To Download Order Details in CSV")
    #     with self.page.expect_download() as download_info:
    #         csv_download_btn.click()
    #     download = download_info.value
    #     download.save_as(f'downloads/{download.suggested_filename}')
        # self.page.pause()

    import os

    def download_csv(self):
        # Wait for the button to be visible
        csv_download_btn = self.page.locator("button:has-text('Click To Download Order Details in CSV')")
        csv_download_btn.wait_for(state="visible")  # Wait until the button is visible on the page

        # Execute the JavaScript to capture the blob
        csv_content = self.page.evaluate("""
        () => {
            const button = Array.from(document.querySelectorAll('.btn.btn-primary'))
                .find(btn => btn.innerText.trim() === 'Click To Download Order Details in CSV');

            if (!button) {
                throw new Error("CSV Download button not found");
            }

            // Override createObjectURL to capture blob content
            window._intercepted_csv = '';
            const originalCreateObjectURL = URL.createObjectURL;
            URL.createObjectURL = function(blob) {
                const reader = new FileReader();
                reader.onload = () => {
                    window._intercepted_csv = reader.result;
                };
                reader.readAsText(blob);
                return originalCreateObjectURL.call(this, blob);
            };

            button.click();

            return new Promise(resolve => {
                setTimeout(() => resolve(window._intercepted_csv), 3000);
            });
        }
        """)

        # Ensure the 'downloads' directory exists before saving the file
        download_dir = "downloads"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Save the CSV content to a file
        filename = os.path.join(download_dir, "order_details.csv")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(csv_content)

        print(f"CSV content saved to: {filename}")

