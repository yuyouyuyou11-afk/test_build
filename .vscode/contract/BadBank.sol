// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.30;

contract BadBank {
    address public owner;
    mapping(address => uint256) public balances;

    constructor() {
        owner = msg.sender;
    }

    // ❌ 使用 tx.origin 进行鉴权（易被钓鱼攻击）
    modifier onlyOwner() {
        require(tx.origin == owner, "not owner");
        _;
    }

    // ❌ 未检查的算术（solc <0.8），可被溢出利用
    function bonus(uint256 b) external {
        balances[msg.sender] += b; // Slither: arithmetic issues
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value; // 同样是未检查加法
    }

    // ❌ 可重入：先外部调用，再更新状态（典型“Checks-Effects-Interactions”顺序错误）
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "not enough");
        // 外部调用（可被攻击者合约回调）
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "send failed");
        // 状态在外部调用之后才修改 -> 可重入
        balances[msg.sender] -= amount;
    }

    // ❌ 不安全的“随机数”：使用区块时间/哈希（可被矿工或验证者影响）
    function random() external view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, blockhash(block.number - 1))));
    }

    // ❌ 可将 owner 设为零地址（缺少校验），且鉴权本身就不安全（tx.origin）
    function setOwner(address newOwner) external onlyOwner {
        owner = newOwner;
    }

    // ❌ 可被误用/滥用的 selfdestruct（鉴权同样使用 tx.origin）
    function destroy() external onlyOwner {
        selfdestruct(payable(msg.sender));
    }
}