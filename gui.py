import wx
from core import CoreModule

class ModulesManagerFrame(wx.Frame):
    def __init__(self, parent, title="Module Manager"):
        super(ModulesManagerFrame, self).__init__(parent, title=title)
        self.core = CoreModule()
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # 添加按钮和对应的事件绑定
        self.buttons = {
            "Read File": self.OnReadFile,
            "Write File": self.OnWriteFile,
            "Execute Command": self.OnExecuteCommand,
            "Send Network Request": self.OnSendNetworkRequest,
            "Send Socket Request": self.OnSendSocketRequest,
            "Write JSON to File": self.OnWriteJSONToFile,
            "Read JSON from File": self.OnReadJSONFromFile,
        }

        for label, handler in self.buttons.items():
            button = wx.Button(self.panel, label=label)
            button.Bind(wx.EVT_BUTTON, handler)
            self.sizer.Add(button, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(self.sizer)
        self.Fit()

    def OnReadFile(self, event):
        # 示例：读取文件
        file_path = "/path/to/your/file.txt"
        content = self.core.read_file(file_path)
        wx.MessageBox(f"File content:\n{content}", "Read File", wx.OK | wx.ICON_INFORMATION)

    def OnWriteFile(self, event):
        # 示例：写入文件
        file_path = "/path/to/your/file.txt"
        self.core.write_file(file_path, "Hello, World!")
        wx.MessageBox("File written successfully", "Write File", wx.OK | wx.ICON_INFORMATION)

    def OnExecuteCommand(self, event):
        # 示例：执行命令
        command = "echo Hello, World!"
        result = self.core.execute_command(command)
        wx.MessageBox(f"Command result:\n{result}", "Execute Command", wx.OK | wx.ICON_INFORMATION)

    def OnSendNetworkRequest(self, event):
        # 示例：发送网络请求
        url = "http://example.com"
        response = self.core.send_network_request(url)
        wx.MessageBox(f"Network response:\n{response}", "Send Network Request", wx.OK | wx.ICON_INFORMATION)

    def OnSendSocketRequest(self, event):
        # 示例：发送基于socket的请求
        host = "localhost"
        port = 8080
        message = "Hello, Server!"
        response = self.core.send_socket_request(host, port, message)
        wx.MessageBox(f"Socket response:\n{response}", "Send Socket Request", wx.OK | wx.ICON_INFORMATION)

    def OnWriteJSONToFile(self, event):
        # 示例：将JSON数据写入文件
        file_path = "/path/to/your/file.json"
        data = {"key": "value"}
        self.core.json_to_file(file_path, data)
        wx.MessageBox("JSON written to file", "Write JSON to File", wx.OK | wx.ICON_INFORMATION)

    def OnReadJSONFromFile(self, event):
        # 示例：从文件读取JSON数据
        file_path = "/path/to/your/file.json"
        data = self.core.file_to_json(file_path)
        wx.MessageBox(f"JSON data:\n{data}", "Read JSON from File", wx.OK | wx.ICON_INFORMATION)

# 运行应用程序
if __name__ == '__main__':
    app = wx.App(False)
    frame = ModulesManagerFrame(None)
    frame.Show()
    app.MainLoop()